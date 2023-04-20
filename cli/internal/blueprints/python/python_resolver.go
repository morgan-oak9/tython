package python

import (
	"bytes"
	"errors"
	"fmt"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"

	"oak9.io/tython/internal/util"
)

const (
	oak9PackageName string = "oak9.tython"
)

var (
	oak9RunnerFilePath = filepath.FromSlash("/oak9/tython/runner.py")
)

func GetPythonRunnerPackagePath() (string, error) {
	pythonVersion, err := checkPythonVersion()
	if err != nil {
		return "", errors.New("[Error] Issue finding python runtime and/or version")
	}

	// Try finding python site packages path and concatenating runner path
	if absolutePath, err := findPythonSitePackagesPath(pythonVersion, oak9RunnerFilePath); err == nil {
		return absolutePath, nil
	}

	// Could not find the site packages path.  Check if oak9 package is installed
	if absolutePath, err := findPythonPackageLocation(oak9PackageName); err == nil {
		return absolutePath, nil
	}

	fmt.Println("[Error] Could not find oak9 Tython Framework package in your global, virtual environment, or user site package directories")
	return "", errors.New("[Error] Could not find oak9 Tython package location")
}

func checkPythonVersion() (int, error) {
	cmd := exec.Command("python", "--version")
	output, err := cmd.CombinedOutput()
	if err != nil {
		return -1, err
	}

	py_version := strings.Split(string(output), ".")[0]
	version := strings.Split(py_version, " ")[1]
	intVar, err := strconv.Atoi(version)

	return intVar, err
}

func RunPythonCommand(commandArgs []string) (string, error) {
	stdout := bytes.Buffer{}
	stderr := bytes.Buffer{}

	cmd := exec.Command("python", commandArgs...)
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	err := cmd.Run()

	if err != nil {
		return "", err
	}

	return stdout.String(), nil
}

func findPythonSitePackagesPath(pythonVersion int, oak9RunnerFilePath string) (string, error) {
	if pythonVersion == 2 {
		return "", errors.New("[Error] Python 3.11 or higher is required")
	}

	notFoundErr := errors.New("[Error] Could not find site packages")
	sitePackagesPath, sitePackagesPathErr := findSitePackagesPathPython3(oak9RunnerFilePath)

	absolutePath := ""
	if sitePackagesPathErr != nil {
		// Could not find site packages; Try the user site package
		userSitePackagesPath, userSitePackagesPathErr := findPythonUserSitePackages(oak9RunnerFilePath)
		if userSitePackagesPathErr != nil {
			return "", notFoundErr
		}
		absolutePath = userSitePackagesPath
	} else {
		absolutePath = sitePackagesPath
	}

	if pathCheck, _ := util.CheckPath(absolutePath); pathCheck {
		return absolutePath, nil
	}

	return absolutePath, notFoundErr
}

func findPythonUserSitePackages(oak9RunnerFilePath string) (string, error) {
	commandUserSite := []string{"-m", "site --user-site"}
	stdout, err := RunPythonCommand(commandUserSite)
	if err != nil {
		return "", errors.Join(errors.New("[Warning] Could not find user site packages"), err)
	}

	output := strings.TrimSpace(stdout)
	runnerAbsolutePath := filepath.Join(output, oak9RunnerFilePath)

	return runnerAbsolutePath, nil
}

func findSitePackagesPathPython3(oak9RunnerFilePath string) (string, error) {
	commandSysConfigGetPath := []string{"-c", "import sysconfig; print(sysconfig.get_paths()[\"purelib\"])"}
	stdout, err := RunPythonCommand(commandSysConfigGetPath)
	if err != nil {
		return "", errors.Join(errors.New("[Warning] Could not find site packages for python3"), err)
	}

	output := strings.TrimSpace(string(stdout))
	runnerAbsolutePath := filepath.Join(output, oak9RunnerFilePath)

	return runnerAbsolutePath, nil

}

func findPythonPackageLocation(oak9PackageName string) (string, error) {
	commandFindPackage := []string{"-c", "\"import " + oak9PackageName + " as _; print(_.__path__)\""}
	stdout, err := RunPythonCommand(commandFindPackage)
	if err != nil {
		return "", errors.Join(fmt.Errorf("[Warning] Could not find package: %s", oak9PackageName), err)
	}

	runnerAbsolutePath := strings.TrimSpace(stdout)
	pathCheck, _ := util.CheckPath(runnerAbsolutePath)

	if pathCheck {
		return runnerAbsolutePath, nil
	}

	return "", fmt.Errorf("[Warning] Could not find package: %s", oak9PackageName)
}
