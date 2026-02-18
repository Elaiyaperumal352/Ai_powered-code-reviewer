from flask import Flask, render_template, request
from reviewer.parser import CodeParser
from reviewer.analysis import StaticAnalyzer
from reviewer.ai_engine import AIReviewEngine
from reviewer.metrics import MetricsCalculator
from reviewer.report import ReportGenerator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    report = None

    if request.method == "POST":

        code = request.form.get("code")

        if code:

            # 1️⃣ Parse
            parser = CodeParser(code)
            functions = parser.extract_functions()
            classes = parser.extract_classes()

            # 2️⃣ Analyze
            analyzer = StaticAnalyzer(code)
            issues = analyzer.run_all_checks()

            # 3️⃣ AI Suggestions
            ai_engine = AIReviewEngine(issues)
            suggestions = ai_engine.generate_suggestions()

            # 4️⃣ Metrics
            metrics_obj = MetricsCalculator(code).generate_metrics()

            # 5️⃣ Report
            reporter = ReportGenerator(
                functions,
                classes,
                issues,
                suggestions,
                metrics_obj
            )

            report = reporter.generate_full_report()

    return render_template("index.html", report=report)


if __name__ == "__main__":
    app.run(debug=True)
