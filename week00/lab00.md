# Lab 00: Setup verification

**Due**: Not graded (optional)
**Points**: 0 (testing only)

## Objective

Verify your development environment and GitHub Actions CI/CD are working correctly.

## Background

This is a **setup verification lab** - not actual course content. It contains two trivially simple functions to ensure:
1. Your Python environment works
2. pytest runs correctly
3. GitHub Actions triggers and passes

Once this lab passes, you'll know your setup is correct for the real course labs.

## Instructions

### Step 1: Create lab00.py

In the `week00/` folder, create a file named `lab00.py` with two simple functions:

```python
# lab00.py
# Setup verification - not actual course content

def hello_world():
    """
    Returns a simple greeting string.

    This function is intentionally trivial - it's only for testing your setup.

    Returns
    -------
    str
        The string "Hello, IS4010!"
    """
    return "Hello, IS4010!"


def add_numbers(a, b):
    """
    Adds two numbers together.

    This function is intentionally trivial - it's only for testing your setup.

    Parameters
    ----------
    a : int or float
        First number
    b : int or float
        Second number

    Returns
    -------
    int or float
        The sum of a and b
    """
    return a + b
```

### Step 2: Run tests locally

```bash
cd week00/
pytest tests/ -v
```

**Expected output:**
```
tests/test_lab00.py::test_hello_world PASSED
tests/test_lab00.py::test_add_numbers PASSED

======================== 2 passed in 0.05s ========================
```

### Step 3: Commit and push

```bash
git add week00/
git commit -m "Complete Week 00 setup verification"
git push origin main
```

### Step 4: Verify GitHub Actions

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. Find the "Week 00 - Setup Verification" workflow
4. Verify it shows a green checkmark ✅

## Success Criteria

✅ Both functions defined correctly
✅ Local tests pass with pytest
✅ GitHub Actions shows green checkmark
✅ You understand the weekly workflow

## What's Next?

Once this lab passes, you're ready to start **Week 01** - the actual course content begins there.

This lab proves:
- Your Python installation works
- Your virtual environment is activated (if using one)
- pytest is installed
- GitHub Actions can run your code
- You know how to commit, push, and verify

**Week 00 is just for testing - don't overthink it!**
