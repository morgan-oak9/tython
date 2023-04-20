package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
	"oak9.io/tython/internal/configurator"
)

var (
	orgId  string
	projId string
	apiKey string
)

var configCmd = &cobra.Command{
	Use:   "config [view|set]",
	Short: "View, set, or update configuration.",
	Long: `This command will let you view, set, or update configuration values for the CLI.
Any value configured this way will be used for future commands unless specifically overridden.`,
	Args: cobra.MinimumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		switch args[0] {
		case "view":
			return configurator.ViewConfig()
		case "set":
			return configurator.SetConfig(cmd.PersistentFlags())
		default:
			return fmt.Errorf("[Error] Please choose either 'view' or 'set' for configuration")
		}
	},
}

func init() {
	rootCmd.AddCommand(configCmd)

	configCmd.PersistentFlags().StringVarP(&orgId, "orgId", "o", "", "The organization id of your oak9 account.")
	configCmd.PersistentFlags().StringVarP(&projId, "projectId", "p", "", "The oak9 project id you want to associate a validation with.")
	configCmd.PersistentFlags().StringVarP(&apiKey, "apiKey", "k", "", "The api key created with oak9. Required for access to upload results.")
}
