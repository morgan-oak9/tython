package viewers

import (
	"io"

	"oak9.io/tython/internal/visuals"
)

type BlueprintOutputViewer struct {
	OutputLines []string
}

func (viewer BlueprintOutputViewer) View(writers ...io.Writer) error {
	if err := visuals.DrawSectionSeparator(writers...); err != nil {
		return err
	}

	if len(viewer.OutputLines) == 0 {
		return nil
	}

	err := visuals.WriteTitle("Blueprint output:", writers...)
	if err != nil {
		return err
	}

	err = visuals.SkipNLines(1, writers...)
	if err != nil {
		return err
	}

	for _, line := range viewer.OutputLines {
		err := visuals.WriteLine(line, writers...)
		if err != nil {
			return err
		}
	}

	return nil
}
