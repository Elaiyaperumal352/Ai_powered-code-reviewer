import sys
from reviewer.parser import CodeParser
from reviewer.analysis import StaticAnalyzer

def run_cli(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    parser = CodeParser(code)
    analyzer = StaticAnalyzer(code)

    print("Functions:", parser.extract_functions())
    print("Classes:", parser.extract_classes())
    print("Issues:", analyzer.run_all_checks())

if __name__ == "__main__":
    run_cli(sys.argv[1])
