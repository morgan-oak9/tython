from typing import Protocol, runtime_checkable, Set
from py.core.finding import Finding


@runtime_checkable
class SupportsValidation(Protocol):
    def validate(self) -> Set[Finding]:
        """
        Entry point into validation logic
        """


class Runner:

    @staticmethod
    def run(validation_target: SupportsValidation):
        print(validation_target.validate())
