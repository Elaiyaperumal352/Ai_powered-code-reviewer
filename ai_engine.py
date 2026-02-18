class AIReviewEngine:

    def __init__(self, issues):
        self.issues = issues

    def generate_suggestions(self):
        suggestions = []
        for issue in self.issues:
            if "docstring" in issue["message"].lower():
                suggestions.append({
                    "suggestion": "Add a proper Google-style docstring explaining parameters and return values."
                })
            elif "long" in issue["message"].lower():
                suggestions.append({
                    "suggestion": "Refactor this function into smaller reusable functions."
                })
            else:
                suggestions.append({
                    "suggestion": "Review this section for improvement."
                })
        return suggestions
