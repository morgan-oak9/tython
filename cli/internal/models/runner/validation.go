package runner

type Validation struct {
	Name        string   `json:"name"`
	Description string   `json:"description"`
	Implements  []Policy `json:"implements"`
	References  []Policy `json:"references"`
	Coverage    string   `json:"coverage"`
}
