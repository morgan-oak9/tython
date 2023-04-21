package enums

type FindingType int

const (
	InvalidFindingType FindingType = iota
	DesignGap
	Kudos
	Warning
	Task
	ResourceGap
)
