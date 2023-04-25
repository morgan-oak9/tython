package configurator

import (
	"bytes"
	"encoding/json"
	"errors"
	"fmt"

	"github.com/spf13/viper"
	"oak9.io/tython/internal/models/config"
	"oak9.io/tython/internal/visuals"
)

const (
	orgIdPrompt     string = "Organization Id (orgId):"
	projectIdPrompt string = "Project Id (projId):"
	apiKeyPrompt    string = "API Key,"
	apiKeyHint      string = "(If you do not have an API Key please first create a Tython integration in the integrations tab at https://console.oak9.io/):"
)

func runWizard() error {
	config := config.CliConfig{}
	err := viper.Unmarshal(&config)
	if err != nil {
		return err
	}

	wizardErrors := []error{
		visuals.DrawSectionSeparatorWithTitle("We need a little more info to get started:"),
		resolveValue(orgIdPrompt, "", func() string { return config.OrgId }, func(val string) { config.OrgId = val }),
		resolveValue(projectIdPrompt, "", func() string { return config.ProjectId }, func(val string) { config.ProjectId = val }),
		resolveValue(apiKeyPrompt, apiKeyHint, func() string { return config.ApiKey }, func(val string) { config.ApiKey = val }),
	}

	json, err := json.Marshal(config)
	if err != nil {
		return err
	}

	cleanViper := viper.New()
	resolveConfigFile(cleanViper)

	if err = cleanViper.ReadConfig(bytes.NewBuffer(json)); err != nil {
		return err
	}

	if err = cleanViper.WriteConfig(); err != nil {
		return err
	}

	if _, err = LoadConfiguration(); err != nil {
		return err
	}

	return errors.Join(wizardErrors...)
}

func resolveValue(fieldName string, hint string, getter func() string, setter func(string)) error {
	if getter() == "" {
		if val, err := promptUserForValue(fieldName, hint); err != nil {
			return err
		} else {
			setter(val)
		}
		visuals.SkipNLines(1)
	}

	return nil
}

func promptUserForValue(fieldName string, hint string) (string, error) {
	if err := visuals.WriteTitle(fmt.Sprintf("Please enter a value for your %s", fieldName)); err != nil {
		return "", err
	}

	if hint != "" {
		if err := visuals.WriteSubTitle(hint); err != nil {
			return "", err
		}
	}

	val := ""
	var err error = nil

	_, err = fmt.Scanln(&val)

	return val, err
}
