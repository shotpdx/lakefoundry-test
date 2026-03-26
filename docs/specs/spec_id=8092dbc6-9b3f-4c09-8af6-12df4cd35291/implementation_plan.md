# Hello World Python Script Implementation Plan

> **For Tech Lead:** REQUIRED SUB-SKILL: Invoke the `lakefoundry-subagent-development` skill to implement this plan task-by-task.

**Goal:** Create a simple Python hello world project with `src/hello.py` that prints "Hello World" and a `README.md` describing the project.

**Architecture:** A minimal Python script lives in `src/hello.py`. A `tests/` directory holds a pytest test that captures stdout and verifies the output. A `README.md` at the project root describes the project.

**Tech Stack:** Python 3, pytest

---

### Task 1: Hello World Script with Test

**Files:**
- Create: `src/hello.py`
- Create: `tests/test_hello.py`

**Step 1: Write the failing test**

```python
# tests/test_hello.py
import subprocess
import sys

def test_hello_prints_hello_world():
    result = subprocess.run(
        [sys.executable, "src/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.stdout.strip() == "Hello World"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_hello.py::test_hello_prints_hello_world -v`
Expected: FAIL with "No such file or directory" or similar error because `src/hello.py` doesn't exist yet.

**Step 3: Write minimal implementation**

```python
# src/hello.py
print("Hello World")
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_hello.py::test_hello_prints_hello_world -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/hello.py tests/test_hello.py
git commit -m "feat: add hello world script with test"
```

---

### Task 2: Add README

**Files:**
- Modify: `README.md`

**Step 1: Update README.md with project description**

Replace the contents of `README.md` with:

```markdown
# lakefoundry-test

A simple Python hello world project.

## Usage

```bash
python src/hello.py
```

Output:
```
Hello World
```

## Running Tests

```bash
pytest
```
```

**Step 2: Verify README exists and is correct**

Run: `cat README.md`
Expected: File contains the project description and usage instructions.

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: update README with project description and usage"
```
