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

from typing import Set
import oak9.tython.core.tools as Tools
# ---- Cloud Resource Models (Protos) --------------------------------
from oak9.tython.models.aws.aws_kms_pb2 import KMS
# ---- Core Types ----------------------------------------------------
from oak9.tython.core.types import Blueprint, Finding, FindingType, DesignGap, Severity, WellDoneRating, ResourceMetadata

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
    # Validation Function Definition
    # ---------------------------------------------------------------------

    # Define validation functions to check specific resource configuration 
    # properties that may lead to potential security risks within your organization. 
    # We recommend constructing these validations in accordance with best coding 
    # practices, which can be found in the Python documentation

    def my_first_validation(self, resource: KMS, resource_metadata: ResourceMetadata):
        """
        A reader-friendly description for your first validation function

        SecurityReq:
            Industry/Organizational requirement this validation applies to

        Author:
            your-name@your-org-email.io

        Returns:
            Finding: DesignGap, Kudos, Warning, Task, ResourceGap
        """

        # ---------------------------------------------------------------------
        # Validation Structure
        # ---------------------------------------------------------------------

        # Initialize a list of findings to return after this function is executed
        your_new_finding = None

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
        # effect how you can access and iterate through these attributes.
        # 
        # First attempt to validate if the object you are attempting to 
        # validate is populated to prevent false positives in your
        # validation results
        # ---------------------------------------------------------------------
        if not resource.HasField("key"):
            return None
        
        config_to_validate = resource.key.description

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
            your_new_finding = Finding(
                finding_type=FindingType.DesignGap,
                # ---------------------------------------------------------------------
                # Specify a config_id relating to the resource config this function
                # was created to validate. Defining this value allows us to perform
                # remediation and provide more detailed DesignGap feedback in console
                # ---------------------------------------------------------------------
                config_id = Tools.get_config_id(resource, "description", resource.key),
                # ---------------------------------------------------------------------
                # Use preferred_values to provide the recommended or required value(s) for
                # your organizational use-case. oak9 will use these values for 
                # code remediation when you specify a repository integration
                # ---------------------------------------------------------------------
                preferred_value = secure_value,
                # ---------------------------------------------------------------------
                # Add a description to your Finding, try embedding [configId] and
                # [preferredValues] here to provide more context to this output 
                # ---------------------------------------------------------------------
                desc = (f"Verbal output you want to be displayed for this "
                        "finding on oak9 console. Include useful information here "
                        "to help your team troubleshoot and resolve issues if "
                        "automatic oak9 remediation is not possible"),
                # ---------------------------------------------------------------------
                # Specify a Finding severity to assist teams in classifying
                # and prioritizing validation results
                # ---------------------------------------------------------------------
                rating = Severity.Critical,
                # ---------------------------------------------------------------------
                # Define a requirementID to assist in categorizing like validation 
                # results based on organizational security requirements
                # ---------------------------------------------------------------------
                req_id="requirementID",
                # ---------------------------------------------------------------------
                # Track the current value of your configuration to assist in giving
                # more context for Finding results and remediation
                # ---------------------------------------------------------------------
                current_value=config_to_validate,
                # ---------------------------------------------------------------------
                # Pass resource metadata to the Findings object
                # ---------------------------------------------------------------------
                resource_metadata=resource_metadata,
                # ---------------------------------------------------------------------
                # Pass target resource to the Findings object
                # ---------------------------------------------------------------------
                resource=resource.key,
            )
        # ---------------------------------------------------------------------
        # And it's that easy! You've just built your first Tython blueprint.
        # Go celebrate by checking out your findings in oak9 console and
        # patching up all the security flaws in your code!
        # ---------------------------------------------------------------------
        return your_new_finding
    

    # ---------------------------------------------------------------------
    # Validation Function Caller
    # ---------------------------------------------------------------------
    def validate(self) -> Set[Finding]:
        
        # ---------------------------------------------------------------------
        # After building out your Tython blueprint, the final step is defining 
        # a caller method that will run all specified validation functions.
        # This step uses the find_by_resource method from our SDK to populate the
        # relevant proto model with data from your cloud infrastructure
        # ---------------------------------------------------------------------  
        resources = self.find_by_resource(KMS)

        findings = set()

        for resource, resource_metadata in resources:
            findings.add(self.my_first_validation(resource, resource_metadata))

        return findings