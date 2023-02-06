from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Set, Any
from py.core.tools import OrderedEnum
from py.core.finding import Finding


class CSP(Enum):
    Aws = 1
    Azure = 2
    GCP = 3


class DataSensitivity(OrderedEnum):
    Sensitive = 2
    NonSensitive = 1


class BusinessImpact(OrderedEnum):
    High = 3
    Medium = 2
    Low = 1


class DeploymentModel(Enum):
    Private = 3
    Hybrid = 2
    Public = 1


class InteractionModel(Enum):
    B2B = 3
    B2C = 2
    B2W = 1


@dataclass
class Context:
    csp: CSP
    data_sensitivity: DataSensitivity
    business_impact: BusinessImpact
    deployment_model: DeploymentModel
    interaction_model: InteractionModel


class BlueprintType(Enum):
    Component = 1
    Reference = 2
    Solution = 3
    Resource = 4
    Customer = 5  # Use this type


class Blueprint:
    blueprint_type: ClassVar[BlueprintType] = BlueprintType.Customer
    id: ClassVar[str] = None
    version: ClassVar[str] = None

    def __init__(self, architecture: Any, context: Context = None, design_pref=None) -> None:
        self._architecture = architecture
        self._context = context
        self._design_pref = design_pref

    @property
    def context(self):
        return self._context

    @property
    def resource(self):
        return self._architecture

    def validate(self) -> Set[Finding]:
        pass
