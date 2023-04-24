# ---------------------------------------------------------------------
# Welcome to the Tython Security as Code 'Hello, World!' Blueprint
# ---------------------------------------------------------------------
# In this blueprint we will build out a few simple examples of
# real use-cases for Tython implementation

# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------
from typing import Set
from oak9.tython.models.aws.aws_kms_pb2 import Key
from oak9.tython.core.types import Blueprint, Finding, FindingType, DesignGap, Severity, WellDoneRating, ResourceMetadata

# ---------------------------------------------------------------------
# Class Definition
# ---------------------------------------------------------------------
class KeyInspector(Blueprint):
    """
    Validate KMS security properties.

    Author:
        squirrel@acorncorp.io
    """

    # ---------------------------------------------------------------------
    # Function Definitions
    # ---------------------------------------------------------------------
    def validate_key_tagging(self, kms: Key, resource_metadata: ResourceMetadata):
        """
        A simple example validation to see if proper tagging
        practices are being followed for KMS keys. This validation
        checks that tags are defined and a specific environment
        tag is included in the 'tags' attribute map

        CustomerReq:
            AssetInventory

        Implements:
            AWS: https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html

        Author:
            squirrel@acorncorp.io

        Returns:
            Finding: DesignGap, Kudos
        """

        findings : list = []

        tags = kms.tags

        if not tags or ('environment' not in tags.keys()):
            NoKeyTags = Finding(FindingType.DesignGap)
            NoKeyTags.resource_metadata=resource_metadata
            NoKeyTags.severity = Severity.Critical
            NoKeyTags.config_id = (tags)
            NoKeyTags.desc = (f"Define [configId] to maintain a proper asset inventory. "
                              "Organizational conventions require that each resource contains "
                              "at least an environment tag, to ensure that the assets are easily "
                              "identifiable and accounted for.")

        else:
            KeyTags = Finding(FindingType.Kudos)
            KeyTags = "By adding this tag you have made it easier to maintain a proper asset inventory"
            KeyTags.rating = WellDoneRating.Good

        return findings

    def validate_deletion_window(self, kms: Key, resource_metadata: ResourceMetadata):
        """
        Validate key deletion window is less than 10 days

        CustomerReq:
            KeyManagement

        Implements:
            AWS: https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html

        Author:
            squirrel@acorncorp.io

        Returns:
            Finding: DesignGap
        """

        findings : list = []

        deletion_window = kms.pending_window_in_days
        max_retention_days = 10

        DecreaseDeletionWindow = Finding(
            resource_metadata=resource_metadata,
            finding_type=FindingType.DesignGap,
            config_id=deletion_window,
            preferred_value=max_retention_days,
            desc=(f"Define [configId] to a value less than [preferredValues] to "
                   "ensure deleted keys are not retained for longer than "
                   "absolutely necessary."),
            severity=Severity.Critical
        )

        if deletion_window > max_retention_days:
            findings.append(DecreaseDeletionWindow)

        return findings

    # ---------------------------------------------------------------------
    # Validation Caller
    # ---------------------------------------------------------------------
    def validate(self) -> Set[Finding]:

        resources = self.find_by_resource(Key)

        findings = set()

        for resource, resource_metadata in resources:
            findings.add(self.validate_key_tagging(resource, resource_metadata))
            findings.add(self.validate_deletion_window(resource, resource_metadata))

        return findings