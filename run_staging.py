import pytest
import sys

if __name__ == "__main__":
    print("🚀 Running Approved Automation Staging Suite...")
    exit_code = pytest.main([r"C:\Dev Projects 2026 Local\GIT\ai_qa_framework\tests\staging", "-v", "-s"])
    sys.exit(exit_code)
