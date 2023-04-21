package runner

type Runner interface {
	Run(runnerArgs RunnerArgs, tempFilePath string) (string, error)
}
