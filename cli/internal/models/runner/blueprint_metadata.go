package runner

type BlueprintMetadata struct {
	Name        string       `json:"name"`
	Desc        string       `json:"desc"`
	Author      string       `json:"author"`
	Validations []Validation `json:"validations"`
}
