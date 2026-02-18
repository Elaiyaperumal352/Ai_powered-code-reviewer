import ast

class CodeParser:

    def __init__(self, code):
        self.code = code
        self.tree = ast.parse(code)

    def extract_functions(self):
        functions = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "lineno": node.lineno
                })

        return functions

    def extract_classes(self):
        classes = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                classes.append({
                    "name": node.name,
                    "lineno": node.lineno
                })

        return classes
