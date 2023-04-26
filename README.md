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

Windows and Linux users can download the CLI binary from the [releases page](https://github.com/oak9io/tython/releases). It is recommended to add the CLI binary to your PATH so Tython commands can be executed from any directory.

## Step 2: Initialize a Tython project utilizing the Python SDK
With the Tython CLI in tow, we're ready to write security rules for our cloud infrastructure. The below example initializes a new Tython module in a blank directory that utilizes the Python SDK.

```
mkdir my-blueprints
cd my-blueprints
tython init python
```

The `tython init python` command will pull in the files necessary to get started creating a Tython module. This includes:
```
module.yml
requirements.txt
my_first_blueprint.py
```

Each of these files is playing a critical role in the Tython module lifecycle:

### module.yml
In order to properly execute Tython blueprint modules, we need metadata about the contents of the blueprints. Today module.yml is quite lean, but oak9 is maintaining a roadmap that will expand on the power that Tython can offer. In the meantime, you'll notice that module.yml contains a `runtime` field set to `python`. This tells the Tython CLI that our security blueprint utilizes the Python SDK.

### requirements.txt
requirements.txt is a widely used convention in the Python community for specifying dependencies of a Python project. It allows developers to list out the required packages and their versions in a plain text file, which can be used to install those packages easily using pip.

To install all Tython dependencies, we can use pip:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### my_first_blueprint.py
This is our templated blueprint file and where the power of Tython will really begin to shine! Continue on to Step 3 to get started writing your first Tython blueprint. Be sure to read through the comments and examples listed in the file for some blueprint-writing hints.

## Step 3: Write a validation rule

For a real-world example of a security blueprint, check out our fully functional [hello_world.py](https://github.com/oak9io/tython/blob/main/templates/python/hello_world.py)!

TODO: Define and describe each major concept to writing blueprints:
* validate() method
* traversing models & namespace imports
* capability id? \ requirement id? (Seems to be required for remediation today. This should be part of a larger discussion)
* resource_metadata
* preferred_values
* config_id
* severity
* findings and returning them
* what else?

Note: Understanding how to write blueprints is a Domain Specific Language on its own and deserves a dedicated tutorial from the oak9 Security Team. Additional info about the Hello World example blueprint should go here as well 

## Step 4: Sign up for oak9 and create a project 

Now that we've written some security rules, we can test them against cloud infrastructure. Behind the scenes, Tython uses oak9's backend to scan cloud resources and prepare them for analysis. Before we can supply our fresh security blueprint with cloud infrastructure data, we need to sign up for a free Community Edition license of oak9 at [oak9.io](https://oak9.io). After finishing the sign-up process, you can create an oak9 project with a code repository integration. oak9 has many other project types, but the Tython Beta support is limited to projects with code repository integrations. Other types may work, they may not; we'd love your feedback if you try other project types! For help getting started with oak9 and projects, visit these documentation resources:

* [https://docs.oak9.io/oak9/guides/creating-your-first-project](https://docs.oak9.io/oak9/guides/creating-your-first-project)
* [https://docs.oak9.io/oak9/fundamentals/integrations/code-repositories/set-up-github](https://docs.oak9.io/oak9/fundamentals/integrations/code-repositories/set-up-github)

Feel free to use your own Infrastructure as Code, but to get started with some example resources, oak9 provides several "insecure by design" Terraform repositories called "Terraoak" that we recommend forking. Please note that the Tython Beta is limited to 200 cloud resources if you do decide to use your own IaC. Additionally, oak9 only supports AWS, Azure, and GCP [Terraform](https://www.terraform.io/) as well as [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

## Step 4a(optional): Fork one of the Terraoak repositories
Try forking one of our Terraoak IaC repositories for some sample cloud resources for your blueprints:

* [https://github.com/oak9io/terraoak.aws](https://github.com/oak9io/terraoak.aws)
* [https://github.com/oak9io/terraoak.azure](https://github.com/oak9io/terraoak.azure)

## Step 5: Obtain an oak9 Tython API Key
At this point we can configure the Tython CLI to reach out to the oak9 API and pull in the cloud resources associated with our new project. These fetched resources can be run against the blueprint we've just created for feedback, but first we need to authorize the CLI for communication with oak9. Start by adding a new oak9 Integration:

![alt text](/templates/screenshots/oak9-add-integration.png "Add oak9 Tython Integration")

![alt text](/templates/screenshots/tython-key-gen.png "Generate Tython API Key")

We can configure the Tython CLI using the command shown on-screen. In this example we can pass the following command to the CLI to get set up with using our project's cloud resources:

```
tython config set -o tythonisprettycool -p proj-tythonisprettycool-1 -k MyTythonKeyThatIWillKeepSecret
```

## Step 6: Execute your blueprint against your IaC
This is where the magic begins! Tython offer two ways to check your IaC against your defined security blueprints:

`tython test ./`

and

`tython apply ./`

### Test

The `test` command will pull in the cloud resources defined in your specified oak9 project and check them against any blueprints in the directory. After completion, Tython reports on what it found in your terminal.

### Apply

The `apply` command acts very similarly to `test`, but also checks your IaC against oak9's blueprint library. The findings from both your own blueprint and oak9's can be viewed in the oak9 console when using the `apply` command.

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