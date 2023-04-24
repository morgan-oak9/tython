package cmd

import (
	"github.com/spf13/cobra"
	"oak9.io/tython/internal/blueprints"
	"oak9.io/tython/internal/constants/enums"
)

var applyCmd = &cobra.Command{
	Use:     "apply [Blueprints package path]",
	Short:   "Applies blueprints, displays any findings, and persists results.",
	Long:    `This command runs blueprints and uses the stored configuration to persist the results via an integration with oak9.`,
	Args:    cobra.MinimumNArgs(1),
	PreRunE: blueprints.UseBlueprintRunFlags,
	RunE: func(cmd *cobra.Command, args []string) error {
		runnerArgs, err := blueprints.BuildRunnerArgs(enums.CmdTypeApply)
		if err != nil {
			return err
		}

		return blueprints.RunBlueprints(*runnerArgs)
	},
}

func init() {
	rootCmd.AddCommand(applyCmd)
}
