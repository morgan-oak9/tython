package blueprints

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/spf13/viper"
	"gopkg.in/yaml.v3"
	"oak9.io/tython/internal/blueprints/python"
	"oak9.io/tython/internal/constants"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/models/outputs"
	"oak9.io/tython/internal/util"
)

const (
	tempDirectoryName  = "tython_temp"
	runnerArgsFileName = "tython_runner_input"
	responseFileName   = "tython_runner_output"
)

func RunBlueprints(runnerArgs outputs.RunnerArgs) error {
	fmt.Println("Applying blueprints...")
	return callRunner(runnerArgs)
}

func TestRunBlueprints(runnerArgs outputs.RunnerArgs) error {
	fmt.Println("Testing blueprints...")
	return callRunner(runnerArgs)
}

func callRunner(runnerArgs outputs.RunnerArgs) error {
	var err error

	runnerArgs.DataConfigPath, err = util.GetAbsolutePath(viper.GetString(config.InputFilePathKey))
	if err != nil {
		return err
	}

	absoluteBlueprintPath, err := util.GetAbsolutePath(runnerArgs.BlueprintPackagePath)
	if err != nil {
		return err
	}

	blueprintRuntime, err := GetRunTimeFromPackage(absoluteBlueprintPath)
	if err != nil {
		return err
	}

	switch blueprintRuntime {
	case constants.PythonRunTime:
		return runWithPython(runnerArgs)
	default:
		return errors.New("[Error] No runtime or unsupported runtime found. Cannot run blueprints")
	}
}

func runWithPython(runnerArgs outputs.RunnerArgs) error {

	pyRunnerPackagePath, err := python.GetPythonRunnerPackagePath()
	if err != nil {
		return errors.Join(
			errors.New("[Error] oak9 Tython framework package is not installed. Be sure to run \"pip install -r requirements.txt\""),
			err,
		)
	}

	tempDirName, tempFilePath, err := saveRunnerArgs(runnerArgs)
	cmdArgs := []string{"-X", "utf8", pyRunnerPackagePath, tempFilePath}
	if err != nil {
		return err
	}

	defer cleanupRunnerArgs(tempDirName)

	cmd := exec.Command("python", cmdArgs...)
	stdout, cmdErr := cmd.CombinedOutput()

	if cmdErr != nil {
		return cmdErr
	}

	fmt.Println(string(stdout))
	return nil
}

func saveRunnerArgs(runnerArgs outputs.RunnerArgs) (tempDir string, tempFilePath string, err error) {
	argsFile := make([]byte, 0)

	argsFile, err = json.Marshal(runnerArgs)
	if err != nil {
		return "", "", err
	}

	tempDir = filepath.Join(os.TempDir(), tempDirectoryName)

	if err = os.Mkdir(tempDir, os.ModeDir); err != nil {
		if !os.IsExist(err) {
			return "", "", err
		}
	}

	file, err := os.CreateTemp(tempDir, fmt.Sprintf("%s*.json", runnerArgsFileName))
	if err != nil {
		return tempDir, "", err
	}
	defer file.Close()

	file.Write(argsFile)
	return tempDir, file.Name(), nil
}

func cleanupRunnerArgs(tempDirPath string) error {
	if filepath.Base(tempDirPath) != tempDirectoryName {
		return errors.New("could not clean up non-temp folder")
	}

	if _, err := os.Stat(tempDirPath); err == nil {
		// Removes the entire Tython temp folder each time to ensure non-persistence
		// Only one copy of the CLI may run simultaneously in this regard
		return os.RemoveAll(tempDirPath)
	}

	return errors.New("did not find temp folder to delete")
}

func GetRunTimeFromPackage(blueprintPackagePath string) (string, error) {
	invalidPublishFileErr := errors.New("[Error] Could not read publish.yml. Cannot determine runtime for blueprints")

	yamlFile, err := os.ReadFile(filepath.FromSlash(filepath.Join(blueprintPackagePath + "/publish.yml")))
	if err != nil {
		return "", invalidPublishFileErr
	}

	data := config.PublishConfig{}

	err = yaml.Unmarshal(yamlFile, &data)
	if err != nil {
		return "", invalidPublishFileErr
	}

	return data.Runtime, nil
}
