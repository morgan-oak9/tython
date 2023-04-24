package repository

import (
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"

	"oak9.io/tython/internal/visuals"
)

const (
	exampleUrlTemplate string = "https://oak9-createuserrole.s3.us-east-2.amazonaws.com/tython-init-examples/%s/%s"
)

func GetExampleFiles(targetDir string, language string, filenames ...string) error {
	if language == "" || len(filenames) == 0 {
		return errors.New("no example files to download")
	}

	getErrs := []error{
		visuals.DrawSectionSeparatorWithTitle(fmt.Sprintf("Downloading example blueprint package for %s", language)),
	}

	for _, filename := range filenames {
		res, err := http.Get(fmt.Sprintf(exampleUrlTemplate, language, filename))
		if err != nil {
			getErrs = append(getErrs, fmt.Errorf("could not download example file %s for %s", filename, language))
			continue
		}
		defer res.Body.Close()

		localPath := filepath.Join(targetDir, filename)
		exampleFile, err := os.Create(localPath)
		if err != nil {
			getErrs = append(getErrs, fmt.Errorf("could not create %s locally for %s", localPath, language))
			continue
		}
		defer exampleFile.Close()

		_, err = io.Copy(exampleFile, res.Body)
		if err != nil {
			getErrs = append(getErrs, fmt.Errorf("could not save example file %s for %s", filename, language))
			continue
		}

		getErrs = append(getErrs, visuals.WriteLine(fmt.Sprintf("Downloaded %s", filename)))
	}

	getErrs = append(getErrs, visuals.DrawSectionSeparator())

	return errors.Join(getErrs...)
}
