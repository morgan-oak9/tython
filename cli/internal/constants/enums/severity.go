package enums

type Severity struct {
	value string
}

func (s Severity) String() string {
	return s.value
}

var (
	SeverityLow      Severity = Severity{"Low"}
	SeverityModerate Severity = Severity{"Moderate"}
	SeverityHigh     Severity = Severity{"High"}
	SeverityCritical Severity = Severity{"Critical"}
)
