package configurator

import (
	"fmt"
)

func ViewConfig() error {
	if configuration, err := LoadConfiguration(); err != nil {
		return err
	} else {
		fmt.Printf("%s", configuration)
	}

	return nil
}
