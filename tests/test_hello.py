"""Tests for the hello world script."""
import subprocess
import sys
from pathlib import Path


def test_hello_prints_hello_world():
    """Verify that running src/hello.py prints 'Hello World' to stdout."""
    script_path = Path(__file__).parent.parent / "src" / "hello.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello World"
