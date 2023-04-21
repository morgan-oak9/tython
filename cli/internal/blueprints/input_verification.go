package blueprints

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"oak9.io/tython/internal/configurator"
	"oak9.io/tython/internal/constants/enums"
	"oak9.io/tython/internal/constants/keys"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/models/runner"
)

func BuildRunnerArgs(cmdType enums.CmdType) (*runner.RunnerArgs, error) {
	cliConfig := &config.CliConfig{}
	viper.Unmarshal(&cliConfig)

	return &runner.RunnerArgs{
		CliConfig:            *cliConfig,
		BlueprintPackagePath: viper.GetString(keys.BlueprintPackagePathKey),
		Mode:                 cmdType.String(),
		DataEndpoint:         viper.GetString(keys.EndpointConfigKey),
	}, nil
}

func SetupBlueprintRunFlags(cmd *cobra.Command) {
	cmd.Flags().String(keys.EndpointConfigKey, "", "Send results to this endpoint for persistance instead")
	cmd.Flags().MarkHidden(keys.EndpointConfigKey)
	viper.BindPFlags(cmd.Flags())
}

func UseBlueprintRunFlags(cmd *cobra.Command, args []string) error {
	if _, err := os.Stat(args[0]); err != nil {
		fmt.Println("Must provide a path to the blueprints you wish to run.")
		return err
	}

	if err := configurator.ViewConfig(); err != nil {
		return err
	}

	viper.Set(keys.BlueprintPackagePathKey, args[0])
	if err := AssertRequiredConfig(); err != nil {
		return err
	}

	return nil
}

func AssertRequiredConfig() error {
	cliConfig := &config.CliConfig{}
	viper.Unmarshal(&cliConfig)

	return cliConfig.AssertAllRequired()
}
