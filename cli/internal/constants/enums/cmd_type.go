package enums

type CmdType struct {
	value string
}

func (cmdType CmdType) String() string {
	return cmdType.value
}

var (
	CmdTypeApply CmdType = CmdType{"apply"}
	CmdTypeTest  CmdType = CmdType{"test"}
)
