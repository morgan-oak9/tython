package viewers

import (
	"encoding/json"
	"io"
	"os"
	"strings"

	"oak9.io/tython/internal/models/runner"
	"oak9.io/tython/internal/visuals"
)

type ResponseViewer struct {
	runnerOutputFileName string
	runnerStdOutput      string
	runnerStdErrOutput   string
	runnerError          error
	response             *runner.RunnerResponse
}

func ViewerFromRunnerOutput(tempFileInputName string, stdOutput string, stdErrOutput string, err error) ResponseViewer {
	return ResponseViewer{
		runnerOutputFileName: strings.ReplaceAll(tempFileInputName, "input", "output"),
		runnerStdOutput:      stdOutput,
		runnerStdErrOutput:   stdErrOutput,
		runnerError:          err,
		response:             &runner.RunnerResponse{},
	}
}

func (viewer *ResponseViewer) View(writers ...io.Writer) error {
	if err := viewer.readResponse(writers...); err != nil {
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

func (viewer *ResponseViewer) readResponse(writers ...io.Writer) error {
	if viewer.runnerError != nil {
		if viewer.runnerStdErrOutput != "" {
			visuals.WriteTitle("Runner Errors:", writers...)
			visuals.SkipNLines(1, writers...)
			visuals.WriteLine(viewer.runnerStdErrOutput, writers...)
		} else {
			visuals.WriteSubTitle("No Other Error Info From Runner", writers...)
		}

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
