package viewers

import (
	"bytes"
	"io"
	"os"
	"testing"

	"github.com/stretchr/testify/assert"
	"oak9.io/tython/internal/models/runner"
)

func TestViewDisplaysAllFindings(t *testing.T) {
	viewer := FindingsViewer{
		Findings: []runner.Finding{
			{
				Rating:  "Low",
				Desc:    "Pass A test",
				ReqName: "TestRequirementNameA",
			},
			{
				Rating:  "Critical",
				Desc:    "Pass B test",
				ReqName: "TestRequirementNameB",
			},
		},
	}

	buf := bytes.Buffer{}
	writer := io.Writer(&buf)
	viewer.View(os.Stdout, writer)

	assert.Contains(t, buf.String(), "Low  Pass A test")
	assert.Contains(t, buf.String(), "TestRequirementNameA")

	assert.Contains(t, buf.String(), "Critical  Pass B test")
	assert.Contains(t, buf.String(), "TestRequirementNameB")
}
