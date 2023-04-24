package python

import (
	"oak9.io/tython/internal/constants"
	"oak9.io/tython/internal/init/repository"
)

const (
	BlueprintFile   string = "my_first_blueprint.py"
	ModuleFile      string = "module.yml"
	RequirementFile string = "requirements.txt"
)

func InitPython(directory string) error {
	exampleFiles := []string{
		BlueprintFile,
		ModuleFile,
		RequirementFile,
	}

	return repository.GetExampleFiles(directory, constants.PythonRunTime, exampleFiles...)
}
