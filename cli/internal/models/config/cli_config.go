package config

import (
	"fmt"

	"oak9.io/tython/internal/util"
	"oak9.io/tython/internal/visuals"
)

const (
	NotSetValue string = "[NOT SET]"
)

type CliConfig struct {
	OrgId     string `mapstructure:"org_id" json:"org_id"`
	ProjectId string `mapstructure:"project_id" json:"project_id"`
	ApiKey    string `mapstructure:"api_key" json:"api_key"`
}

func (config *CliConfig) String() string {
	return fmt.Sprintf("%s, %s, %s", config.OrgId, config.ProjectId, showLastN(config.ApiKey, 4))
}

func (config *CliConfig) View() error {
	errs := []error{
		visuals.DrawSectionSeparatorWithTitle("Configuration"),
		visuals.WriteKeyValue("Org Id", config.OrgId),
		visuals.WriteKeyValue("Project Id", config.ProjectId),
		visuals.WriteKeyValue("Api Key", showLastN(config.ApiKey, 4)),
		visuals.DrawSectionSeparator(),
	}

	for _, err := range errs {
		if err != nil {
			return err
		}
	}

	return nil
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
