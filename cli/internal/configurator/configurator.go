package configurator

import (
	"encoding/json"
	"os"
	"path/filepath"

	"github.com/spf13/viper"
	"oak9.io/tython/internal/models/config"
)

const (
	configurationFolder   string = "tython"
	configurationFilename string = ".configuration"
)

func LoadConfiguration() (*config.CliConfig, error) {
	if err := resolveConfigFile(viper.GetViper()); err != nil {
		return nil, err
	}

	if err := viper.ReadInConfig(); err != nil {
		return nil, err
	}

	config := &config.CliConfig{}
	viper.Unmarshal(&config)

	return config, nil
}

func AssertAllRequired(config *config.CliConfig) ([]string, error) {
	invalidConfig := make([]string, 0, 3)

	if config.OrgId == "" {
		invalidConfig = append(invalidConfig, "orgId")
	}

	if config.ProjectId == "" {
		invalidConfig = append(invalidConfig, "projectId")
	}

	if config.ApiKey == "" {
		invalidConfig = append(invalidConfig, "apiKey")
	}

	if len(invalidConfig) > 0 {
		return invalidConfig, runWizard()
	}

	return invalidConfig, nil
}

func resolveConfigFile(v *viper.Viper) error {
	home := ""
	var err error

	if home, err = os.UserHomeDir(); err != nil {
		return err
	}

	configFolder := filepath.Join(home, configurationFolder)

	if _, err := os.Stat(configFolder); err != nil {
		if os.IsNotExist(err) {
			os.Mkdir(configFolder, 0644)
		} else {
			return nil
		}
	}

	configFilePath := filepath.Join(configFolder, configurationFilename)

	if _, err := os.Stat(configFilePath); err != nil {
		if os.IsNotExist(err) {
			file := &os.File{}
			file, err = os.Create(configFilePath)
			if err != nil {
				return err
			}

			defer file.Close()

			baseConfig := config.CliConfig{}
			jsonBaseConfig, err := json.Marshal(baseConfig)
			if err != nil {
				return err
			}

			_, err = file.Write(jsonBaseConfig)
			if err != nil {
				return err
			}
		}
	}

	v.SetConfigFile(configFilePath)
	v.SetConfigType("json")

	return nil
}
