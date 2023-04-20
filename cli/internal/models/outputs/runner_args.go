package outputs

import (
	"oak9.io/tython/internal/constants/enums"
	"oak9.io/tython/internal/models/config"
)

type RunnerArgs struct {
	config.CliConfig
	RuntimePath          string           `json:"runtime_path"`
	BlueprintPackagePath string           `json:"blueprint_package_path"`
	DataSource           enums.DataSource `json:"data_source"`
	DataEndpoint         string           `json:"data_endpoint"`
	DataConfigPath       string           `json:"data_config_path"`
	ProjectEnvironmentId string           `json:"project_environment_id"`
	RequestId            string           `json:"request_id"`
	Mode                 enums.CmdType    `json:"mode"`
}
