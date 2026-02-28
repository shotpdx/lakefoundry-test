"""Tests for the hello world module."""
import io
import sys

from src.hello import main


def test_hello_world_output():
    """Verify that main() prints 'Hello World' to stdout."""
    captured = io.StringIO()
    sys.stdout = captured
    try:
        main()
    finally:
        sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "Hello World"
