# Tython
Security as Code Framework

Tython is an open source security as code framework from [oak9](https://www.oak9.io) that lets you define security reference architectures as code (blueprints) in the language of your choice. Internally, oak9 uses this same framework to codify security blueprints that adhere to industry standard guidance from NIST, Cloud Security Alliance (CSA), AWS, Azure, GCP and others. This open source project enables developers and security professionals to build their own blueprints and contribute them back to the community.

# Getting Started
If you're interested in trying your hand at writing some security blueprints of your own and testing out the Tython framework, follow along with our Python example below. 

## Step 1: Get the Tython CLI
To get started writing your own security blueprints with the Tython framework, head to the [releases page](https://github.com/oak9io/tython/releases) to download and install the CLI. Platform-specific instructions can be found below.

### MacOS\Homebrew
[Homebrew](https://brew.sh/) users can easily install the Tython CLI by adding the tython tap repository:

```
brew tap oak9io/tap
brew install tython
```
When a new version of the CLI is released, tython can be updated with the following Homebrew command

```
brew update
brew reinstall tython
```

### Windows

Windows users can download the binary from the releases page and add a folder to their path with the Powershell command below. This assumes the directory the binary has been copied to is "C:\TythonCLI".

```
[Environment]::SetEnvironmentVariable("PATH", $Env:PATH + ";C:\TythonCLI", [EnvironmentVariableTarget]::Machine)
```

## Step 2: Initialize a Tython project utilizing the Python SDK
With the Tython CLI in tow, we're ready to write security rules for our cloud infrastructure. The below example initializes a new Tython module in a blank directory that utilizes the Python SDK.

```
mkdir my-blueprints
cd my-blueprints
tython init python
```

To install all of Tython dependencies, we can use pip:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Step 3: Write a validation rule


## Step 4: Sign up for oak9 and create a project 

## Step 4a(optional): Fork one of the Terraoak repositories

## Step 5: Obtain an oak9 Tython API Key

`tython config`

## Step 6: Execute your blueprint against your IaC

## Step 7: Results in the oak9 console and remediation steps

## Guiding Principles

* Empower the community to collaborate, build, and share security best practices
* Strive for simplicity and extensibility
* Focus on value to security and dev teams
* Build reusable security reference architectures
* Create transparency in the security design
* Enable collaboration, autonomy, and shared responsibility across Dev and Security
* Consider the lifecycle management of security architectures
* Enable scalable security reference architectures
* Cloud and technology agnostic approach

## Background

Tython not only happens to be the birthplace of the Je'Daii Order (a precursor to the Jedi), it also is a portmanteau for the first two programming languages that we have built support for - Typescript and Python.

## Feedback
We welcome contributions! If you are interested in participating feel free to create a GitHub issue or open a pull request. For support, questions, or to simply say "Hi!", join us on Discord: https://discord.gg/YHjfEfYYjz or reach out to tython@oak9.io.