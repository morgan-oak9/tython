package runner

type RelatedConfig struct {
	ConfigId       string      `json:"config_id"`
	ConfigValue    interface{} `json:"config_value"`
	PreferredValue interface{} `json:"preferred_value"`
	Comment        string      `json:"comment"`
}
