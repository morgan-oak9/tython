package enums

type DataSource struct {
	value string
}

func (ds DataSource) String() string {
	return ds.value
}

var (
	DataSourceLocal DataSource = DataSource{"local"}
	DataSourceOak9  DataSource = DataSource{"oak9"}
)
