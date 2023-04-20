package util

import (
	"os"
	"path/filepath"
	"strings"
)

func GetAbsolutePath(path string) (string, error) {
	homedir, err := os.UserHomeDir()
	if err != nil {
		return "", err
	}

	if path == "~" {
		path = homedir
	} else if strings.HasPrefix(path, "~/") {
		path = filepath.Join(homedir, path[2:])
	}

	absPath, _ := filepath.Abs(path)
	return filepath.FromSlash(absPath), nil
}

func CheckPath(path string) (bool, error) {
	_, err := os.Stat(path)
	return err == nil, err
}
