# Hello World Python Script Implementation Plan

> **For Tech Lead:** REQUIRED SUB-SKILL: Invoke the `lakefoundry-subagent-development` skill to implement this plan task-by-task.

**Goal:** Create a simple Python hello world project with `src/hello.py` and a `README.md`.

**Architecture:** A minimal Python script in `src/hello.py` that prints "Hello World" when executed directly. A `README.md` at the project root describes the project. Tests verify the script's output using subprocess.

**Tech Stack:** Python 3, pytest

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
    assert result.stdout.strip() == "Hello World"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_hello.py::test_hello_world_output -v`
Expected: FAIL with "No such file or directory" or similar error

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
- Modify: `README.md`

**Step 1: Write the README**

```markdown
# lakefoundry-test

A simple Python hello world project.

## Usage

```bash
python src/hello.py
```

Prints:
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
Expected: File contains project description and usage instructions.

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add README with project description and usage"
```
