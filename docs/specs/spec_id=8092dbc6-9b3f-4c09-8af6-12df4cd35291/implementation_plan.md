# Hello World Python Script Implementation Plan

> **For Tech Lead:** REQUIRED SUB-SKILL: Invoke the `lakefoundry-subagent-development` skill to implement this plan task-by-task.

**Goal:** Create a simple Python hello world project with a `src/hello.py` script and a `README.md`.

**Architecture:** A minimal Python script in `src/hello.py` that prints "Hello World". A `README.md` at the project root describes the project. Tests live in `tests/` and verify the script's output.

**Tech Stack:** Python 3, pytest, subprocess (for output capture in tests)

---

### Task 1: Create `src/hello.py` with Hello World output

**Files:**
- Create: `src/hello.py`
- Create: `tests/test_hello.py`

**Step 1: Write the failing test**

```python
# tests/test_hello.py
import subprocess
import sys

def test_hello_world_output():
    result = subprocess.run(
        [sys.executable, "src/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "Hello World" in result.stdout
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_hello.py::test_hello_world_output -v`
Expected: FAIL with "No such file or directory" or similar error (src/hello.py doesn't exist yet)

**Step 3: Write minimal implementation**

```python
# src/hello.py
print("Hello World")
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_hello.py::test_hello_world_output -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/hello.py tests/test_hello.py
git commit -m "feat: add hello world script with test"
```

---

### Task 2: Create README.md

**Files:**
- Create: `README.md`

**Step 1: Write the README**

```markdown
# Hello World

A simple Python hello world project.

## Usage

```bash
python src/hello.py
```

This will print:

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
Expected: File exists and contains project description and usage instructions.

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add README with project description and usage"
```
