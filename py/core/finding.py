from enum import Enum
from py.core.tools import OrderedEnum


class Severity(OrderedEnum):
    Critical = 4
    High = 3
    Moderate = 2
    Low = 1


class FindingType(Enum):
    DesignGap = 1
    Warning = 2
    ResourceGap = 3


class Finding:

    def __init__(self, finding_type: FindingType, desc: str = "", fix: str = "",
                 rating: Severity = Severity.Low) -> None:
        self._finding_type: FindingType = finding_type
        self._desc: str = desc
        self._fix: str = fix
        self._rating: Severity = rating

    @property
    def finding_type(self):
        return self._finding_type

    @finding_type.setter
    def finding_type(self, value):
        self._finding_type = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    @property
    def fix(self):
        return self._fix

    @fix.setter
    def fix(self, value):
        self._fix = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
