import os
import pylint.lint

def run_pylint():
    """Run PyLint analysis on the project and generate a report."""
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    pylint_opts = [
        "--rcfile=.pylintrc",
        "--output-format=colorized",
        "--reports=y",
        "--score=y"
    ]

    report_file = os.path.join(reports_dir, "pylint_report.txt")
    with open(report_file, "w", encoding="utf-8") as f:
        pylint.lint.Run([".", *pylint_opts], reporter=pylint.reporters.BaseReporter(f))

    print(f"PyLint report generated: {report_file}")

if __name__ == "__main__":
    run_pylint()