import pytest
import sys

if __name__ == "__main__":
    print("🚀 Running Approved Automation Staging Suite...")
    # Scans the directory and runs all valid test functions cleanly
    exit_code = pytest.main(["tests/staging", "-v", "-s"])
    sys.exit(exit_code)
