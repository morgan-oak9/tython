package viewers

import (
	"fmt"
	"io"

	"oak9.io/tython/internal/models/runner"
	"oak9.io/tython/internal/visuals"
)

type BlueprintMetadataViewer struct {
	MetadataList []runner.BlueprintMetadata
}

func (viewer BlueprintMetadataViewer) View(writers ...io.Writer) error {
	if err := visuals.DrawSectionSeparator(writers...); err != nil {
		return err
	}

	if len(viewer.MetadataList) == 0 {
		visuals.WriteTitle("Did not find any blueprints to run!", writers...)
		return nil
	}

	visuals.DrawSectionSeparatorWithTitle(fmt.Sprintf("Ran %d Blueprints", len(viewer.MetadataList)), writers...)
	for i, metadata := range viewer.MetadataList {
		errs := []error{
			visuals.WriteTitle(fmt.Sprintf("Blueprint #%d", i+1), writers...),
			visuals.SkipNLines(1),
			visuals.WriteKeyValue("Name", metadata.Name, writers...),
			visuals.WriteKeyValue("Description", metadata.Desc, writers...),
			visuals.WriteKeyValue("Author", metadata.Author, writers...),
			visuals.WriteKeyValue("Number of validations", fmt.Sprintf("%d", len(metadata.Validations)), writers...),
			visuals.SkipNLines(1),
		}

		for _, err := range errs {
			if err != nil {
				return err
			}
		}
	}

	return nil
}
