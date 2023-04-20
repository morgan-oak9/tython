package configurator

import (
	"bytes"
	"encoding/json"
	"fmt"

	"github.com/iancoleman/strcase"
	"github.com/spf13/pflag"
	"github.com/spf13/viper"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/util"
)

func SetConfig(flags *pflag.FlagSet) error {

	if _, err := LoadConfiguration(); err != nil {
		return err
	}

	if err := resolveFlagOverrides(flags); err != nil {
		return err
	}

	return ViewConfig()
}

func resolveFlagOverrides(flags *pflag.FlagSet) error {
	setFlags := make([]string, 0)

	flags.VisitAll(func(f *pflag.Flag) {
		if f.Changed {
			setFlags = append(setFlags, f.Name)
			viper.Set(strcase.ToSnake(f.Name), f.Value)
		}
	})

	if err := cleanConfig(); err != nil {
		return err
	}

	if len(setFlags) == 0 {
		fmt.Println("No flags were set - no config values were changed.")
	} else {
		fmt.Printf("%s updated successfully.\n", util.FormatListWithTense(setFlags, util.PastTense))
	}

	return viper.WriteConfig()
}

// Restrict values saved in config file to only expected values
func cleanConfig() error {
	persistentConfig := config.CliConfig{}
	err := viper.Unmarshal(&persistentConfig)
	if err != nil {
		return err
	}

	persistentConfigJson := new(bytes.Buffer)
	if err := json.NewEncoder(persistentConfigJson).Encode(persistentConfig); err != nil {
		return err
	}

	return viper.ReadConfig(persistentConfigJson)
}
