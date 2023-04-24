package runner

type Policy struct {
	Name        string `json:"name"`
	Description string `json:"description"`
	Provider    string `json:"provider"`
	Url         string `json:"url"`
}
