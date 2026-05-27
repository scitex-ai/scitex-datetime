"""Compile-only stub for examples/quickstart.py (PS303)."""

import subprocess
import sys
from pathlib import Path

QUICKSTART = Path(__file__).parents[2] / "examples" / "quickstart.py"


def test_quickstart_script_file_exists_on_disk():
    # Arrange
    path = QUICKSTART
    # Act
    is_file = path.is_file()
    # Assert
    assert is_file, f"missing {QUICKSTART}"


def test_quickstart_script_compiles_without_syntax_errors():
    # Arrange
    cmd = [sys.executable, "-m", "py_compile", str(QUICKSTART)]
    # Act
    completed = subprocess.run(cmd, check=False, capture_output=True, text=True)
    # Assert
    assert completed.returncode == 0, completed.stderr
