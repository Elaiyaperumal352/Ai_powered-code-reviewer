from datetime import datetime
from config import Config

class ReportGenerator:

    def __init__(self, functions, classes, issues, suggestions, metrics):
        self.functions = functions
        self.classes = classes
        self.issues = issues
        self.suggestions = suggestions
        self.metrics = metrics

    def calculate_score(self):
        score = 100 - (len(self.issues) * 5)
        return max(score, 0)

    def generate_full_report(self):

        report = {
            "project": Config.PROJECT_NAME,
            "version": Config.VERSION,
            "timestamp": datetime.now().isoformat(),
            "functions": [f["name"] for f in self.functions],
            "classes": [c["name"] for c in self.classes],
            "metrics": {
                "maintainability_index": self.metrics.maintainability_index,
                "average_complexity": self.metrics.average_complexity
            },
            "issues": self.issues,
            "suggestions": self.suggestions,
            "quality_score": self.calculate_score()
        }

        return report
