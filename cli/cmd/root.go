package cmd

import (
	"errors"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

const (
	DefaultConfigJson string = "config.json"
	version           string = "0.0.1"
)

var rootCmd = &cobra.Command{
	Use:   "",
	Short: "oak9 Tython",
	Long: `oak9 Tython is a CLI that enables users to execute their SaC blueprints locally.
Use the help command or '-h' flag for more info.`,
	Version: version,
	Args:    cobra.MinimumNArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		return errors.New("no command chosen - try 'help' or use the '-h' flag to see list of available commands")
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintf(
			os.Stderr,
			"Tython encountered the following error: '%s'",
			err,
		)
		os.Exit(1)
	}
}

func init() {
	rootCmd.CompletionOptions.DisableDefaultCmd = true
}