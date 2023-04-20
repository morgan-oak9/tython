package blueprints

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"oak9.io/tython/internal/configurator"
	"oak9.io/tython/internal/constants/enums"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/models/outputs"
)

func BuildRunnerArgs(cmdType enums.CmdType) (*outputs.RunnerArgs, error) {
	dataSource, validDataSource := viper.Get(config.DataSourceKey).(enums.DataSource)
	if !validDataSource {
		return nil, fmt.Errorf("[Error] Invalid data source specified. Please inspect your paths are correct for this command")
	}

	cliConfig := &config.CliConfig{}
	viper.Unmarshal(&cliConfig)

	return &outputs.RunnerArgs{
		CliConfig:            *cliConfig,
		BlueprintPackagePath: viper.GetString(config.BlueprintPackagePathKey),
		DataSource:           dataSource,
		Mode:                 cmdType,
	}, nil
}

func UseBlueprintRunFlags(cmd *cobra.Command, args []string) error {
	if _, err := os.Stat(args[0]); err != nil {
		fmt.Println("Must provide a path to the blueprints you wish to run.")
		return err
	}

	if err := configurator.ViewConfig(); err != nil {
		return err
	}

	viper.Set(config.BlueprintPackagePathKey, args[0])
	if dataStr := viper.GetString("data"); dataStr != "" {
		viper.Set(config.InputFilePathKey, dataStr)
		viper.Set(config.DataSourceKey, enums.DataSourceLocal)
	} else {
		viper.Set(config.DataSourceKey, enums.DataSourceOak9)
		if err := AssertRequiredConfig(); err != nil {
			return err
		}
	}

	return nil
}

func AssertRequiredConfig() error {
	cliConfig := &config.CliConfig{}
	viper.Unmarshal(&cliConfig)

	return cliConfig.AssertAllRequired()
}
