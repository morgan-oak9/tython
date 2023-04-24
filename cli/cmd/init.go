package cmd

import (
	"fmt"
	"os"
	"strings"

	"github.com/spf13/cobra"
	"oak9.io/tython/internal/constants"
	"oak9.io/tython/internal/init/python"
	"oak9.io/tython/internal/util"
	"oak9.io/tython/internal/visuals"
)

var initCmd = &cobra.Command{
	Use:   "init [language] [directory]",
	Short: "Create a new Tython blueprint package from a template.",
	Long: `Create a new Tython blueprint package in the specified language.
If a directory is provided then the package will be created there, otherwise it will be created in the current directory`,
	Args: cobra.MinimumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) (err error) {
		defer func() {
			if r := recover(); r != nil {
				if len(args) > 0 {
					err = fmt.Errorf("[Error] Could not initialize blueprints for %s", args[0])
				} else {
					err = fmt.Errorf("[Error] An unknown error occurred. Could not initialize blueprints")
				}
			}
		}()

		supportedRuntimes := util.FormatListWithTense([]string{constants.PythonRunTime}, util.PresentTense)

		var initMethod func(string) error

		switch strings.ToLower(args[0]) {
		case constants.PythonRunTime:
			initMethod = python.InitPython
		default:
			return fmt.Errorf("[Error] %s is not currently a supported language. %s currently supported", args[0], supportedRuntimes)
		}

		targetDir, err := os.Getwd()
		if err != nil {
			return err
		}

		if len(args) > 1 {
			targetDir = args[1]
		}

		if _, err = os.Stat(targetDir); err != nil {
			if os.IsNotExist(err) {
				return fmt.Errorf("[Error] Specified directory %s does not exist", targetDir)
			} else if os.IsPermission(err) {
				return fmt.Errorf("[Error] Insufficient permissions to access directory %s to initialize blueprints", targetDir)
			} else {
				return fmt.Errorf("[Error] Could not intialize blueprints in given directory %s", targetDir)
			}
		}

		err = initMethod(targetDir)
		if err != nil {
			return err
		}

		return visuals.WriteTitle(fmt.Sprintf("Successfully initialized %s in %s", args[0], targetDir))
	},
}

func init() {
	rootCmd.AddCommand(initCmd)
}
