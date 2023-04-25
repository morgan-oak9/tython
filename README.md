# Tython
Security as Code Framework

Tython is an open source security as code framework from [oak9](https://www.oak9.io) that lets you define security reference architectures as code (blueprints) in the language of your choice. Internally, oak9 uses this same framework to codify security blueprints that adhere to industry standard guidance from NIST, Cloud Security Alliance (CSA), AWS, Azure, GCP and others. This open source project enables developers and security professionals to build their own blueprints and contribute them back to the community.

# Getting Started
If you're interested in trying your hand at writing some security blueprints of your own and testing out the Tython framework, follow along with our Python example below. 

## Step 1: Get the Tython CLI
To get started writing your own security blueprints with the Tython framework, head to the [releases page](https://github.com/oak9io/tython/releases) to download and install the CLI. Platform-specific instructions can be found below.

### MacOS\Homebrew
[Homebrew](https://brew.sh/) users can easily install the Tython CLI by adding the Tython tap repository:

```
brew tap oak9io/tap
brew install tython
```
When a new version of the CLI is released, the Tython CLI can be updated with the following Homebrew command

```
brew update
brew upgrade tython
```

### Windows and Linux

Windows and Linux users can download the binary from the [releases page](https://github.com/oak9io/tython/releases). It is recommended to add the CLI binary to your PATH so Tython commands can be executed from any directory.

## Step 2: Initialize a Tython project utilizing the Python SDK
With the Tython CLI in tow, we're ready to write security rules for our cloud infrastructure. The below example initializes a new Tython module in a blank directory that utilizes the Python SDK.

```
mkdir my-blueprints
cd my-blueprints
tython init python
```

To install all Tython dependencies, we can use pip:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Step 3: Write a validation rule

Info about Hello World example from template goes here ./templates/python/hello_world.py

## Step 4: Sign up for oak9 and create a project 

Now that we've written some security rules, we can test them against cloud infrastructure. Behind the scenes, Tython uses oak9's backend to scan cloud resources and prepare them for analysis. To get started with some example resources, oak9 provides several "insecure-by-design" Terraform 

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