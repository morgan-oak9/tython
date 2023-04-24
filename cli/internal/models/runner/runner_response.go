package runner

type RunnerResponse struct {
	BlueprintOutput   []string            `json:"blueprint_output"`
	BlueprintMetadata []BlueprintMetadata `json:"blueprint_metadata"`
	BlueprintProblems []string            `json:"blueprint_problems"`
	Findings          []Finding           `json:"findings"`
}
