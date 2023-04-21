package viewers

import (
	"fmt"
	"io"

	"oak9.io/tython/internal/visuals"
)

type BlueprintProblemsViewer struct {
	Problems []string
}

func (viewer BlueprintProblemsViewer) View(writers ...io.Writer) error {
	if len(viewer.Problems) == 0 {
		visuals.WriteTitle("All blueprints ran successfully.", writers...)
		return nil
	}

	visuals.WriteTitle(fmt.Sprintf("%d issue(s) were encountered with blueprints while running:", len(viewer.Problems)), writers...)
	for _, problem := range viewer.Problems {
		visuals.WriteSubTitle(problem, writers...)
	}

	return nil
}
