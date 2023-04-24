package blueprints

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path/filepath"

	"gopkg.in/yaml.v3"
	"oak9.io/tython/internal/blueprints/python"
	"oak9.io/tython/internal/constants"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/models/runner"
	"oak9.io/tython/internal/util"
	"oak9.io/tython/internal/viewers"
	"oak9.io/tython/internal/visuals"
)

const (
	tempDirectoryName  = "tython_temp"
	runnerArgsFileName = "tython_runner_input"
)

func RunBlueprints(runnerArgs runner.RunnerArgs) error {
	visuals.WriteLine("Applying blueprints...")
	return callRunner(runnerArgs)
}

func TestRunBlueprints(runnerArgs runner.RunnerArgs) error {
	visuals.WriteLine("Testing blueprints...")
	return callRunner(runnerArgs)
}

func callRunner(runnerArgs runner.RunnerArgs) error {
	var err error

	absoluteBlueprintPath, err := util.GetAbsolutePath(runnerArgs.BlueprintPackagePath)
	if err != nil {
		return err
	}

	blueprintRuntime, err := getRunTimeFromPackage(absoluteBlueprintPath)
	if err != nil {
		return err
	}

	tempDirName, tempFilePath, err := saveRunnerArgs(runnerArgs)
	defer cleanupRunnerArgs(tempDirName)

	responseViewer := viewers.ResponseViewer{}

	switch blueprintRuntime {
	case constants.PythonRunTime:
		responseViewer = python.Run(runnerArgs, tempFilePath)
	default:
		return errors.New("[Error] No runtime or unsupported runtime found. Cannot run blueprints")
	}

	return responseViewer.View(os.Stdout)
}

func saveRunnerArgs(runnerArgs runner.RunnerArgs) (tempDir string, tempFilePath string, err error) {
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

func getRunTimeFromPackage(blueprintPackagePath string) (string, error) {
	invalidModuleFileErr := errors.New("[Error] Could not read module.yml. Cannot determine runtime for blueprints")

	yamlFile, err := os.ReadFile(filepath.FromSlash(filepath.Join(blueprintPackagePath + "/module.yml")))
	if err != nil {
		return "", invalidModuleFileErr
	}

	data := config.ModuleConfig{}

	err = yaml.Unmarshal(yamlFile, &data)
	if err != nil {
		return "", invalidModuleFileErr
	}

	return data.Runtime, nil
}
