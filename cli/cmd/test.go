package cmd

import (
	"github.com/spf13/cobra"
	"oak9.io/tython/internal/blueprints"
	"oak9.io/tython/internal/constants/enums"
)

var testCmd = &cobra.Command{
	Use:   "test [Blueprints package path]",
	Short: "Run the specified SaC blueprint package as a test run without persisting results.",
	Long: `This command runs blueprints but does not persist the results anywhere.
The results will still be displayed in the terminal for evaluation.
'test' is used during the development of blueprints to ensure they are reporting the correct results.`,
	Args:    cobra.MinimumNArgs(1),
	PreRunE: blueprints.UseBlueprintRunFlags,
	RunE: func(cmd *cobra.Command, args []string) error {
		runnerArgs, err := blueprints.BuildRunnerArgs(enums.CmdTypeTest)
		if err != nil {
			return err
		}

		return blueprints.TestRunBlueprints(*runnerArgs)
	},
}

func init() {
	blueprints.SetupBlueprintRunFlags(testCmd)
	rootCmd.AddCommand(testCmd)
}
