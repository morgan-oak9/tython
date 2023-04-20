package util

import (
	"fmt"
	"strings"
)

const (
	PastTense int = iota
	PresentTense
	FutureTense
)

func FormatListWithTense(strArr []string, tense int) string {
	separator := " "
	if len(strArr) > 2 {
		separator = ", "
	}

	verbTense := "is"

	switch tense {
	case PastTense:
		verbTense = "was"
		if len(strArr) > 1 {
			verbTense = "were"
		}
	case FutureTense:
		verbTense = "will be"
	default:
		if len(strArr) > 1 {
			verbTense = "are"
		}
	}

	if len(strArr) > 1 {
		strArr[len(strArr)-1] = "and " + strArr[len(strArr)-1]
	}

	return fmt.Sprintf("%s %s", strings.Join(strArr, separator), verbTense)
}
