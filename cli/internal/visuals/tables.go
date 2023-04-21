package visuals

import (
	"errors"
	"fmt"
	"io"
	"strings"

	"github.com/fatih/color"
)

func DrawSimpleKeyValueTable(rows map[string]string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	longestKeyLen := 0
	for key := range rows {
		if len(key) > longestKeyLen {
			longestKeyLen = len(key)
		}
	}

	secondColumnStart := longestKeyLen + IndentLength

	for key, value := range rows {
		err := outputToAllStreams(drawKeyValueTableRow(key, value, secondColumnStart), writers...)
		if err != nil {
			return err
		}
	}

	return outputFToAllStreams("", writers...)
}

func DrawSimpleOrderedKeyValueTable(rows map[string]string, order []string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	longestKeyLen := 0

	if len(order) != len(rows) {
		return errors.New("could not organize table of unexpected format")
	}

	for _, key := range order {
		if len(key) > longestKeyLen {
			longestKeyLen = len(key)
		}
	}

	secondColumnStart := longestKeyLen + IndentLength

	for _, orderedKey := range order {
		val := ""
		exists := false

		if val, exists = rows[orderedKey]; !exists {
			return fmt.Errorf("could not display table correctly - the row with key %s is missing", orderedKey)
		}

		err := outputToAllStreams(drawKeyValueTableRow(orderedKey, val, secondColumnStart), writers...)
		if err != nil {
			return err
		}
	}

	return outputFToAllStreams("", writers...)
}

func drawKeyValueTableRow(key string, value string, secondColumnStart int) func(io.Writer) error {
	return func(writer io.Writer) error {
		_, err := color.New(color.FgWhite).Fprintf(
			writer,
			"%s%s",
			key,
			strings.Repeat(" ", secondColumnStart-len(key)),
		)
		if err != nil {
			return err
		}

		_, err = color.New(color.FgHiBlack).Fprintf(
			writer,
			"%s\n",
			value,
		)
		if err != nil {
			return err
		}
		return nil
	}
}
