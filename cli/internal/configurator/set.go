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
	"oak9.io/tython/internal/visuals"
)

func SetConfig(flags *pflag.FlagSet) error {

	if _, err := LoadConfiguration(); err != nil {
		return err
	}

	return resolveFlagOverrides(flags)
}

func resolveFlagOverrides(flags *pflag.FlagSet) error {
	setFlags := make([]string, 0)

	flags.VisitAll(func(f *pflag.Flag) {
		if f.Changed {
			setFlags = append(setFlags, f.Name)
			viper.Set(strcase.ToSnake(f.Name), f.Value)
		}
	})

	config, cleanViper, err := cleanConfig()
	if err != nil {
		return err
	}

	if len(setFlags) == 0 {
		if filledFields, err := fillMissingRequiredValues(config); len(filledFields) == 0 || err != nil {
			if err != nil {
				return err
			}

			if err = ViewConfig(); err != nil {
				return err
			}

			err = visuals.WriteLine("No flags were set - no config values were changed.")
			if err != nil {
				return err
			}

			err = visuals.DrawSectionSeparator()
			if err != nil {
				return err
			}
		}
	} else {
		if err := ViewConfig(); err != nil {
			return err
		}

		if err = visuals.WriteTitle(fmt.Sprintf("%s updated successfully.", util.FormatListWithTense(setFlags, util.PastTense))); err != nil {
			return err
		}

		err = visuals.DrawSectionSeparator()
		if err != nil {
			return err
		}

		if filledFields, err := fillMissingRequiredValues(config); len(filledFields) > 0 || err != nil {
			if err != nil {
				return err
			}

			err = visuals.DrawSectionSeparator()
			if err != nil {
				return err
			}
		} else {
			if err = cleanViper.WriteConfig(); err != nil {
				return err
			}
		}
	}

	return nil
}

func fillMissingRequiredValues(config config.CliConfig) (updateableFields []string, err error) {
	updateableFields, err = AssertAllRequired(&config)

	if err != nil {
		return
	}

	if len(updateableFields) > 0 {
		if err = ViewConfig(); err != nil {
			return
		}

		if err = visuals.WriteTitle("Configuration updated successfully."); err != nil {
			return
		}
	}

	return
}

// Restrict values saved in config file to only expected values
func cleanConfig() (persistentConfig config.CliConfig, cleanViper *viper.Viper, err error) {
	persistentConfig = config.CliConfig{}
	err = viper.Unmarshal(&persistentConfig)
	if err != nil {
		return
	}

	json, err := json.Marshal(persistentConfig)
	if err != nil {
		return
	}

	cleanViper = viper.New()
	resolveConfigFile(cleanViper)

	if err = cleanViper.ReadConfig(bytes.NewBuffer(json)); err != nil {
		return
	}

	return
}
