from radon.metrics import mi_visit
from radon.complexity import cc_visit
from reviewer.models import MetricsModel

class MetricsCalculator:

    def __init__(self, code):
        self.code = code

    def calculate_maintainability(self):
        return mi_visit(self.code, True)

    def calculate_complexity(self):
        complexity_objects = cc_visit(self.code)

        if not complexity_objects:
            return 0

        total = sum(obj.complexity for obj in complexity_objects)
        return total / len(complexity_objects)

    def generate_metrics(self):
        maintainability = self.calculate_maintainability()
        avg_complexity = self.calculate_complexity()

        return MetricsModel(
            maintainability_index=round(maintainability, 2),
            average_complexity=round(avg_complexity, 2)
        )
