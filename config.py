import os

class Config:

    PROJECT_NAME = "AI Code Reviewer"
    VERSION = "2.0.0"

    MAX_COMPLEXITY = 10
    MAX_FUNCTION_LENGTH = 20

    SEVERITY_LEVELS = {
        "info": 1,
        "low": 2,
        "medium": 3,
        "high": 4,
        "critical": 5
    }

    QUALITY_PENALTY = {
        "info": 1,
        "low": 3,
        "medium": 5,
        "high": 8,
        "critical": 12
    }

    REPORT_FOLDER = "reports"
    LOG_FOLDER = "logs"

    EXCLUDED_PATHS = ["venv", "__pycache__", "tests"]

    @staticmethod
    def ensure_directories():
        os.makedirs(Config.REPORT_FOLDER, exist_ok=True)
        os.makedirs(Config.LOG_FOLDER, exist_ok=True)
