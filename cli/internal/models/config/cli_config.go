package config

import (
	"fmt"

	"oak9.io/tython/internal/util"
)

const (
	InputFilePathKey        string = "InputFilePath"
	DataSourceKey           string = "DataSource"
	BlueprintPackagePathKey string = "BlueprintPackagePath"
	CommandTypeKey          string = "CommandType"
)

const (
	NotSetValue string = "[NOT SET]"
)

const ConfigDisplay string = `
================[Configuration]=================
Org Id: %s,
Project Id: %s,
Api Key: %s
================================================
`

type CliConfig struct {
	OrgId     string `mapstructure:"org_id" json:"org_id"`
	ProjectId string `mapstructure:"project_id" json:"project_id"`
	ApiKey    string `mapstructure:"api_key" json:"api_key"`
}

func (config *CliConfig) String() string {
	return fmt.Sprintf(
		ConfigDisplay,
		valueOrDefault(config.OrgId),
		valueOrDefault(config.ProjectId),
		valueOrDefault(showLastN(config.ApiKey, 4)),
	)
}

func (config *CliConfig) AssertAllRequired() error {
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
		return fmt.Errorf("%s missing, but required. Please run 'tython config set [flags]' to set these values", util.FormatListWithTense(invalidConfig, util.PresentTense))
	}

	return nil
}

func valueOrDefault(str string) string {
	if str == "" {
		return NotSetValue
	}

	return str
}

func showLastN(str string, n int) string {
	if str != "" {
		if len(str) > n {
			return fmt.Sprintf("************%s", str[len(str)-n:])
		}
	}

	return str
}
