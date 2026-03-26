import subprocess
import sys

def test_hello_prints_hello_world():
    result = subprocess.run(
        [sys.executable, "src/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Hello World"
