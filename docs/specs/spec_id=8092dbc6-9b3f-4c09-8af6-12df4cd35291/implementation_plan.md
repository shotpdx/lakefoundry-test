# Create a hello world Python script Implementation Plan

> **For Tech Lead:** REQUIRED SUB-SKILL: Invoke the `lakefoundry-subagent-development` skill to implement this plan task-by-task.

**Goal:** Create a minimal Python project that includes `src/hello.py` printing `Hello World` and a `README.md` that documents how to run it.

**Architecture:** Use a simple single-file Python script under a `src/` directory to satisfy the project structure requirement. Add a concise README section describing purpose and run command. Validate behavior by running the script directly.

**Tech Stack:** Python 3, pytest (repository default test tooling), Markdown

---

### Task 1: Create Hello World script in `src/`

**Files:**
- Create: `src/hello.py`
- Test: `src/hello.py` (runtime verification via command execution)

**Step 1: Create project source directory if it does not exist**

Run: `mkdir -p src`
Expected: `src/` directory exists.

**Step 2: Write minimal implementation**

Create `src/hello.py` with:

```python
print("Hello World")
```

**Step 3: Run script to verify required output**

Run: `python src/hello.py`
Expected: `Hello World` printed to stdout.

**Step 4: Commit**

```bash
git add src/hello.py
git commit -m "feat: add hello world python script"
```

### Task 2: Document project usage in README

**Files:**
- Modify: `README.md`
- Test: `README.md` (manual verification of instructions)

**Step 1: Update README with project description and run instructions**

Add a concise section that includes:
- Project purpose (Hello World Python script)
- File location (`src/hello.py`)
- Exact run command:

```bash
python src/hello.py
```

- Expected output:

```text
Hello World
```

**Step 2: Verify README instructions match actual behavior**

Run: `python src/hello.py`
Expected: Output matches README (`Hello World`).

**Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add hello world project usage"
```
