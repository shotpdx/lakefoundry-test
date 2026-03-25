import os


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md does not exist"


def test_readme_describes_project():
    with open("README.md") as f:
        content = f.read()
    assert "hello" in content.lower(), "README.md should mention 'hello'"
    assert "python" in content.lower(), "README.md should mention 'python'"
    assert "src/hello.py" in content, "README.md should reference src/hello.py"
