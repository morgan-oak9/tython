package configurator

func ViewConfig() error {
	configuration, err := LoadConfiguration()
	if err != nil {
		return err
	}

	return configuration.View()
}
