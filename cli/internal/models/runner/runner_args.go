package runner

import (
	"oak9.io/tython/internal/models/config"
)

type RunnerArgs struct {
	config.CliConfig
	BlueprintPackagePath string `json:"blueprint_package_path"`
	DataEndpoint         string `json:"data_endpoint"`
	RequestId            string `json:"request_id"`
	Mode                 string `json:"mode"`
}
