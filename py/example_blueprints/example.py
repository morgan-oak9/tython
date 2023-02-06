from typing import Set
from py.core.types import Blueprint
from py.core.finding import Finding, FindingType

"""
    Example blueprint
"""


# noinspection PyMethodMayBeStatic
class MyBlueprint(Blueprint):
    """

    This is my first example blueprint

    Name:
        Asset Inventory Checks

    Author:
        email@email.com

    """

    def validate_custom_tagging_check(self):
        """
        My custom validation check for asset inventory

        CustomerReq:
            Req.1

        Implements:
            CSA: https://Link_to_CSA
            NIST: https://link_to_nist
            Customer Framework: https://link_to_customer_compliance

        Returns:
            Finding: Security design finding
        """
        print("Running your custom tagging check")

        # *** My validation logic goes here ***

        my_finding = Finding(
            finding_type=FindingType.DesignGap,
            desc="Tags are missing"
        )

        return my_finding

    def validate_custom_naming_check(self):
        """
        My second custom validation check

        CustomerReq:
            Req.2

        Implements:
            CSA: https://Link_to_CSA
            NIST: https://link_to_nist
            Customer Framework: https://link_to_customer_compliance

        Returns:
            Finding: Security design finding
        """
        print("Running my custom naming convention check")

        # *** My validation logic goes here ***

        my_finding = Finding(
            finding_type=FindingType.DesignGap,
            desc="Naming convention is not inline with standards"
        )

        return my_finding

    def validate(self) -> Set[Finding]:
        design_gaps = set()
        design_gaps.add(self.validate_custom_naming_check())
        design_gaps.add(self.validate_custom_tagging_check())
        return design_gaps
