package visuals

import (
	"fmt"
	"io"
	"os"
	"strings"

	"github.com/fatih/color"
)

const (
	BlockLength  int = 42
	IndentLength int = 4
)

func init() {
	// Globally disabled until per output checks can be done
	color.NoColor = true
}

func DrawSectionSeparatorWithTitle(title string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	return outputToAllStreams(drawSectionSeparator(title), writers...)
}

func DrawSectionSeparator(writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	return outputToAllStreams(drawSectionSeparator(""), writers...)
}

func drawSectionSeparator(title string) func(io.Writer) error {
	return func(writer io.Writer) error {
		if title != "" {
			color.New(color.FgHiWhite).Add(color.Bold).Fprint(writer, title)
		}
		_, err := color.New(color.FgHiBlack).Fprintln(writer, fmt.Sprintf("\n%s\n", strings.Repeat("-", BlockLength)))
		return err
	}
}

func SkipNLines(n int, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	skipLine := func(writer io.Writer) error {
		_, err := fmt.Fprint(writer, strings.Repeat("\n", n))
		return err
	}

	return outputToAllStreams(skipLine, writers...)
}

func WriteTitle(txt string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	writeTitle := func(writer io.Writer) error {
		_, titleErr := color.New(color.FgHiWhite).Add(color.Bold).Fprintln(writer, txt)
		return titleErr
	}

	return outputToAllStreams(writeTitle, writers...)
}

func WriteSubTitle(txt string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	writeSubTitle := func(writer io.Writer) error {
		_, titleErr := color.New(color.FgHiBlack).Add(color.Bold).Fprintln(writer, txt)
		return titleErr
	}

	return outputToAllStreams(writeSubTitle, writers...)
}

func WriteKeyValue(key string, value string, writers ...io.Writer) error {
	writers = defaultToStdOut(writers...)

	writeKeyValue := func(writer io.Writer) error {
		_, err := color.New(color.FgWhite).Fprintf(writer, "%s: ", key)
		if err != nil {
			return err
		}

		_, err = color.New(color.FgHiBlack).Fprintln(writer, value)
		if err != nil {
			return err
		}

		return nil
	}

	return outputToAllStreams(writeKeyValue, writers...)
}

func WriteLine(txt string, writers ...io.Writer) (err error) {
	writers = defaultToStdOut(writers...)

	writeLine := func(writer io.Writer) error {
		_, err := color.New(color.FgWhite).Fprintln(writer, txt)
		return err
	}

	return outputToAllStreams(writeLine, writers...)
}

func outputFToAllStreams(txt string, writers ...io.Writer) (err error) {
	for _, writer := range writers {
		_, err = fmt.Fprint(writer, txt)
		if err != nil {
			return
		}
	}

	return nil
}

func outputToAllStreams(write func(io.Writer) error, writers ...io.Writer) (err error) {
	for _, writer := range writers {
		err = write(writer)
		if err != nil {
			return
		}
	}

	return nil
}

func defaultToStdOut(writers ...io.Writer) []io.Writer {
	if len(writers) == 0 {
		return []io.Writer{os.Stdout}
	}

	return writers
}
