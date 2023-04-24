# ---------------------------------------------------------------------
# Welcome to the Tython Security as Code template!
# ---------------------------------------------------------------------
# This template can be used to quickly and easily create blueprints for cloud resources 
# and cloud infrastructure use-cases specific to your needs. By utilizing this template, 
# you can ensure that your cloud resources and infrastructure are secure and compliant 
# with industry standards and best practices. 

# We hope you find this template to be a helpful resource!


# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------
# Tython leverages protobuf models to represent the cloud resource configurations
# that make up your infrastructure. In addition to this we have created a number
# of objects that assist in blueprint logic and validation development. You will
# need to import any of these objects you wish to implement in your blueprint by
# referencing the oak9.tython package

# ---- Cloud Resource Models (Protos) --------------------------------
from oak9.tython.models import *
# ---- Core Types ----------------------------------------------------
from oak9.tython.core.types import *

# ---------------------------------------------------------------------
# Class Definition
# ---------------------------------------------------------------------

# Specify a unique name for your Tython blueprint by defining a new class.

# Adding docstrings to your class and function definitions is an easy and 
# effective way to ensure that your code is well-documented, easy to read, 
# and consistent. It also helps to provide an accessible reference for 
# anyone who needs to work with or modify the code. We recommend adding 
# docstrings to all of your class and function definitions for maximum code 
# readability and maintainability.

class MyFirstBlueprint(Blueprint):
    """
    A reader-friendly description for your first blueprint

    Author:
        your-name@your-org-email.io
    """

    # ---------------------------------------------------------------------
    # Function Definition
    # ---------------------------------------------------------------------

    # Define validation functions to check specific resource configuration 
    # properties that may lead to potential security risks within your organization. 
    # We recommend constructing these validations in accordance with best coding 
    # practices, which can be found in the Python documentation

    def my_first_validation(self, resource: Resource):
        """
        A reader-friendly description for your first validation function

        SecurityReq:
            Industry/Organizational requirement this validation applies to

        Implements:
            Link: www.link-to-external/internal-security-framework.com

        Author:
            your-name@your-org-email.io

        Returns:
            Finding: DesignGap, Kudos, Warning, Task, ResourceGap
        """

        # ---------------------------------------------------------------------
        # Validation Structure
        # ---------------------------------------------------------------------

        # Initialize a list of findings to return after this function is executed
        findings : list = []

        # This is where the oak9.tython resource models and objects we imported earlier 
        # start to come into play. To validate specific properties and configurations for
        # a given resource, you will need to import the corresponding pb2 protobuf model
        # as demonstrated in the imports section. These are located in the tython/py/models
        # directory of our Tython repo. We have intellisense that will help auto-complete our
        # model attributes as you type them out to aid in development. To view the model 
        # definitions for all supported resources please reference the .proto files in the
        # tython/proto directory

        # ---------------------------------------------------------------------
        # Grab the relevant proto config - be aware of types as they will
        # effect how you can access and iterate through these attributes
        # ---------------------------------------------------------------------
        config_to_validate = resource.sub_config.config_you_care_about

        secure_value = "some_secure_value_to_check_for"

        # ---------------------------------------------------------------------
        # Build out your validation logic, this can be as simple as a basic 
        # conditional or as complex as your use-case requires
        # ---------------------------------------------------------------------
        if config_to_validate != secure_value:
            # ---------------------------------------------------------------------
            # Use oak9 Finding objects to classify your validation results and
            # report relevant feedback and information back to your development teams.
            # See tython/core/types for all supported configurations on this object
            # ---------------------------------------------------------------------
            your_new_finding = Finding(FindingType.<DesignGap, Kudos, Warning, Task, ResourceGap>)
            # ---------------------------------------------------------------------
            # Specify a config_id relating to the resource config this function
            # was created to validate. Defining this value allows us to perform
            # remediation and provide more detailed DesignGap feedback in console
            # ---------------------------------------------------------------------
            your_new_finding.config_id = (config_to_validate)
            # ---------------------------------------------------------------------
            # Use preferred_values to provide the recommended or required value(s) for
            # your organizational use-case. oak9 will use these values for 
            # code remediation when you specify a repository integration
            # ---------------------------------------------------------------------
            your_new_finding.preferred_value = secure_value
            # ---------------------------------------------------------------------
            # Add a description to your Finding, try embedding [configId] and
            # [preferredValues] here to provide more context to this output 
            # ---------------------------------------------------------------------
            your_new_finding.desc = (f"Verbal output you want to be displayed for this "
                                      "finding on oak9 console. Include useful information here "
                                      "to help your team troubleshoot and resolve issues if "
                                      "automatic oak9 remediation is not possible")
            # ---------------------------------------------------------------------
            # Specify a Finding severity to assist teams in classifying
            # and prioritizing validation results
            # ---------------------------------------------------------------------
            your_new_finding.severity = Severity.<Low, Moderate, High, Critical>

        # ---------------------------------------------------------------------
        # And it's that easy! You've just built your first Tython blueprint.
        # Go celebrate by checking out your findings in oak9 console and
        # patching up all the security flaws in your code!
        # ---------------------------------------------------------------------
        return findings