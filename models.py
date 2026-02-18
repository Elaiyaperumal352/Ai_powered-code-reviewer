from dataclasses import dataclass
from typing import List, Optional

@dataclass
class FunctionModel:
    name: str
    lineno: int
    args: List[str]
    docstring: Optional[str]

@dataclass
class ClassModel:
    name: str
    lineno: int

@dataclass
class IssueModel:
    category: str
    message: str
    severity: str
    lineno: int

@dataclass
class MetricsModel:
    maintainability_index: float
    average_complexity: float
