package runner

type RunnerResponse struct {
	BlueprintProblems []string  `json:"blueprint_problems"`
	Findings          []Finding `json:"findings"`
}
