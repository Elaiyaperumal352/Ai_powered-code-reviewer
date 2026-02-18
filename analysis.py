import ast

class StaticAnalyzer:

    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)

    def detect_long_functions(self):
        issues = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if len(node.body) > 20:
                    issues.append({
                        "severity": "high",
                        "message": f"Function '{node.name}' is too long."
                    })
        return issues

    def detect_missing_docstrings(self):
        issues = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    issues.append({
                        "severity": "medium",
                        "message": f"Function '{node.name}' has no docstring."
                    })
        return issues

    def run_all_checks(self):
        issues = []
        issues.extend(self.detect_long_functions())
        issues.extend(self.detect_missing_docstrings())
        return issues
