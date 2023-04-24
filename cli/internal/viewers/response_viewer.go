package viewers

import (
	"encoding/json"
	"io"
	"os"
	"strings"

	"oak9.io/tython/internal/models/runner"
)

type ResponseViewer struct {
	runnerOutputFileName string
	runnerStdOutput      string
	runnerError          error
	response             *runner.RunnerResponse
}

func ViewerFromRunnerOutput(tempFileInputName string, output string, err error) ResponseViewer {
	return ResponseViewer{
		runnerOutputFileName: strings.ReplaceAll(tempFileInputName, "input", "output"),
		runnerStdOutput:      output,
		runnerError:          err,
		response:             &runner.RunnerResponse{},
	}
}

func (viewer *ResponseViewer) View(writers ...io.Writer) error {
	if err := viewer.readResponse(); err != nil {
		return err
	}

	blueprintMetadataSection := BlueprintMetadataViewer{
		MetadataList: viewer.response.BlueprintMetadata,
	}

	blueprintProblemsSection := BlueprintProblemsViewer{
		Problems: viewer.response.BlueprintProblems,
	}

	blueprintOutputSection := BlueprintOutputViewer{
		OutputLines: viewer.response.BlueprintOutput,
	}

	findingsSection := FindingsViewer{
		Findings: viewer.response.Findings,
	}

	sections := []Viewer{
		blueprintMetadataSection,
		blueprintProblemsSection,
		blueprintOutputSection,
		findingsSection,
	}

	for _, section := range sections {
		if err := section.View(writers...); err != nil {
			return err
		}
	}

	return nil
}

func (viewer *ResponseViewer) readResponse() error {
	if viewer.runnerError != nil {
		return viewer.runnerError
	}

	runnerResponse, err := os.ReadFile(viewer.runnerOutputFileName)
	if err != nil {
		return err
	}

	if err = json.Unmarshal(runnerResponse, &viewer.response); err != nil {
		return err
	}

	return nil
}
