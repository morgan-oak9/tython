# ---------------------------------------------------------------------
# Welcome to the Tython Security as Code 'Hello, World!' Blueprint
# ---------------------------------------------------------------------
# In this blueprint we will build out a few simple examples of
# real use-cases for Tython implementation

# ---------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------
from typing import Set
import functools
import oak9.tython.core.tools as Tools
from oak9.tython.models.aws.aws_kms_pb2 import KMS
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
    def validate_key_tagging(self, kms: KMS, resource_metadata: ResourceMetadata):
        """
        A simple example validation to see if proper tagging
        practices are being followed for KMS keys. This validation
        checks that tags are defined and a specific environment
        tag is included in the 'tags' attribute map

        CustomerReq:
            AssetInventory
        
        Author:
            squirrel@acorncorp.io

        Returns:
            Finding: DesignGap, Kudos
        """

        finding = None

        if not kms.HasField("key"):
            return None
        
        tags = kms.key.tags

        if not tags or ('environment' not in tags.keys()):
            finding = Finding(
                resource=tags,
                resource_metadata=resource_metadata,
                finding_type=FindingType.DesignGap,
                req_id="test",
                rating = Severity.Critical,
                config_id =Tools.get_config_id(kms, "tags", kms.key),
                current_value= tags,
                desc = (f"Define tags to maintain a proper asset inventory. "
                            "Organizational conventions require that each resource contains "
                            "at least an environment tag to ensure that the assets are easily "
                            "identifiable and accounted for.")
            )

        else:

            finding = Finding(
                resource=tags,
                resource_metadata=resource_metadata,
                finding_type=FindingType.Kudos,
                desc = "By adding this tag you have made it easier to maintain a proper asset inventory",
                rating = WellDoneRating.Good
            )

        return finding

    def validate_deletion_window(self, kms: KMS, resource_metadata: ResourceMetadata):
        """
        Validate key deletion window is less than 10 days

        CustomerReq:
            KeyManagement

        Author:
            squirrel@acorncorp.io

        Returns:
            Finding: DesignGap
        """

        finding = None

        deletion_window = kms.key.pending_window_in_days
        max_retention_days = 10

        if deletion_window > max_retention_days:
            finding = Finding(
                resource=kms.key,
                resource_metadata=resource_metadata,
                finding_type=FindingType.DesignGap,
                config_id=Tools.get_config_id(kms, "pending_window_in_days", kms.key),
                current_value=deletion_window,
                req_id="test",
                preferred_value=max_retention_days,
                desc=(f"Define [configId] to a value less than [preferredValues] to "
                    "ensure deleted keys are not retained for longer than "
                    "absolutely necessary."),
                rating=Severity.Critical
            )

        return finding

    # ---------------------------------------------------------------------
    # Validation Caller
    # ---------------------------------------------------------------------
    def validate(self) -> Set[Finding]:

        resources = self.find_by_resource(KMS)

        findings = set()

        for resource, resource_metadata in resources:
            findings.add(self.validate_key_tagging(resource, resource_metadata))
            findings.add(self.validate_deletion_window(resource, resource_metadata))

        return findings