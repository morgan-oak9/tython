# oak9 Tython CLI 

Tython supports testing and applying (i.e. running) user-created SaC blueprints. This can be done locally on your own machine or through integrations with oak9.

## Supported Commands
```
tython config [view|set] [-o <orgId>] [-p <projectId>] [-k <apiKey>]
tython apply [pathToBlueprints]
tython test [pathToBlueprints]
```

For this B.Y.O.L. (Bring Your Own Language) example, Tython supports following commands:
* `config`
  * View or set configuration for the Tython CLI. Some config must be set first if you want to persist your results with oak9[^1].
* `apply`
  * Apply your SaC blueprints to your cloud resources and receive back a list of security violations. If you have established an oak9 integration then results will be persisted[^1] to your project.
* `test`
  * Run your SaC blueprints locally without persisting results. Used for rapid development, prototyping, and verification that blueprints are working properly before applying them.

[^1]: Please note that as of right now, persistance and PR capabilities are work in progress :)

## Requirements

Go 1.20+

### Go
In order to run the CLI, you will need Go installed on your machine. For more info, please see https://go.dev/ to download and install Go runtime packages for your architecture.
Once you have installed Go, you will need to compile the CLI with following command from the CLI directory - 

    go build

This compiles the oak9 Tython CLI as "tython". If you want to run the CLI from anywhere, you will need to add it to your path variables.
You can test to make sure the CLI works by either using `./tython -v` or `./tython -h` commands, or if using Windows `./tython.exe -v` or `./tython.exe -h`.

### Python
Python 3.11 and higher are supported by Tython. For more info please see https://www.python.org/downloads/ and install a supported version for your architecture.
