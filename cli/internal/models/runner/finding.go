package runner

type Finding struct {
	FindingType        string          `json:"finding_type"`
	Desc               string          `json:"desc"`
	Rating             string          `json:"rating"`
	AdjustedSeverity   string          `json:"adusted_severity"`
	ConfigId           string          `json:"config_id"`
	CurrentValue       string          `json:"current_value"`
	Fix                string          `json:"fix"`
	PreferredValue     string          `json:"preferred_value"`
	AdditionalGuidance string          `json:"additional_guidance"`
	RelatedConfigs     []RelatedConfig `json:"related_configs"`
	RelatedFindings    []string        `json:"related_findings"`
	ReqId              string          `json:"req_id"`
	ReqName            string          `json:"req_name"`
	Priority           int             `json:"priority"`
	DocumentationUrl   string          `json:"documentation_url"`
}
