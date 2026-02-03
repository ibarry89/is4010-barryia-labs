# IS4010 Labs - Common Troubleshooting Guide

This guide covers common problems students encounter across all labs. Each lab README also includes lab-specific troubleshooting for unique issues.

---

## 🐍 Python Issues

### **Problem: "ModuleNotFoundError: No module named 'labXX'"**
- **Cause**: pytest cannot find your Python file
- **Solution**:
  - Ensure `labXX.py` is in the `labXX/` folder (not the root or another folder)
  - Run pytest from the repository root: `pytest labXX/test_labXX.py`
  - Check filename spelling - must be exactly `labXX.py` (lowercase, no spaces)
  - Make sure the file is saved before running tests

### **Problem: "AttributeError: module 'labXX' has no attribute 'function_name'"**
- **Cause**: Function name doesn't match exactly what tests expect
- **Solution**:
  - Function must be named **exactly** as specified in lab instructions
  - Check for typos in function name (case-sensitive)
  - Make sure function is defined at module level (not nested inside another function or `if __name__ == "__main__"` block)
  - Function definition should start with `def function_name(parameters):`

### **Problem: "SyntaxError" or "IndentationError"**
- **Cause**: Python syntax issues
- **Solution**:
  - Check that all parentheses, quotes, and brackets are properly closed
  - Ensure consistent indentation (use 4 spaces, not tabs)
  - Make sure function definitions start with `def` and end with `:`
  - Docstrings must use triple quotes `"""`
  - Use VS Code's Python extension for syntax highlighting
  - Check for missing commas in lists/dictionaries

### **Problem: "My function returns None instead of a value"**
- **Cause**: Forgot to include `return` statement
- **Solution**:
  - Every function needs a `return` statement to send back a value
  - Check that `return` is not inside a loop (usually should be after the loop)
  - Make sure you're returning the correct data type (string, int, list, etc.)
  - `pass` is a placeholder - replace it with actual code and `return`

### **Problem: "ImportError: cannot import name 'X' from 'labXX'"**
- **Cause**: Function doesn't exist or has wrong name
- **Solution**:
  - Make sure function is spelled exactly as specified
  - Function must be defined before the test file tries to import it
  - Check that there are no syntax errors preventing the file from loading

---

## 🧪 Testing Issues

### **Problem: "AssertionError" in tests**
- **Cause**: Your function's output doesn't match expected output
- **Solution**:
  - Read the test error message carefully - it shows expected vs. actual values
  - Test your function manually with the same inputs to debug
  - Check edge cases: empty inputs, None values, special characters
  - Make sure you're returning the exact data type expected (string vs list vs int)

### **Problem: "pytest: command not found"**
- **Cause**: pytest not installed or virtual environment not activated
- **Solution**:
  - Activate your virtual environment:
    - macOS/Linux: `source venv/bin/activate`
    - Windows (Git Bash): `source venv/Scripts/activate`
  - Install pytest: `pip install pytest`
  - Verify installation: `pytest --version`

### **Problem: "No tests ran / 0 tests collected"**
- **Cause**: Test file not found or incorrectly named
- **Solution**:
  - Test files must be named `test_labXX.py` (start with `test_`)
  - Test functions must start with `test_` (e.g., `def test_function_name():`)
  - Make sure test file is in the `labXX/` folder
  - Run from repository root: `pytest labXX/test_labXX.py -v`

---

## 🔧 GitHub Actions / CI/CD Issues

### **Problem: "GitHub Actions workflow not running"**
- **Cause**: Workflow file not in correct location or not triggered
- **Solution**:
  - Workflow file must be in `.github/workflows/` folder
  - Workflow file must end with `.yml` extension
  - Check that you pushed your changes: `git push origin main`
  - Workflow may only trigger on specific paths (check `paths:` in workflow file)

### **Problem: "GitHub Actions badge shows 'failing' but tests pass locally"**
- **Cause**: File not committed, wrong file location, or environment differences
- **Solution**:
  - Make sure you committed AND pushed: `git push origin main`
  - Verify files are in correct location using GitHub web interface
  - Check Actions tab for specific error message
  - Python version in GitHub Actions might differ - check workflow file
  - Re-run the workflow if it was a temporary issue (click "Re-run jobs")

###  **Problem: "GitHub Actions badge not showing or showing 'no status'"**
- **Cause**: Workflow hasn't run yet or badge markdown is incorrect
- **Solution**:
  - Make a commit and push to trigger the workflow
  - Check that workflow file exists in `.github/workflows/`
  - Verify badge URL in README.md matches your repository
  - Wait a few minutes for badge to update after first run

### **Problem: "Workflow permissions error"**
- **Cause**: GitHub Actions doesn't have permission to run
- **Solution**:
  - Go to Settings → Actions → General
  - Under "Workflow permissions", select "Read and write permissions"
  - Save changes and re-run workflow

---

## 📁 File and Directory Issues

### **Problem: "File not found" errors**
- **Cause**: File in wrong location or incorrectly named
- **Solution**:
  - Use exact folder structure shown in lab README
  - File names are case-sensitive: `Lab03.py` ≠ `lab03.py`
  - Check for extra spaces in filenames
  - Use `ls labXX/` to see what files actually exist

### **Problem: "Permission denied" errors**
- **Cause**: File permissions or running from wrong directory
- **Solution**:
  - Make sure you're in the repository root directory
  - Check that files are not open in another program
  - On macOS/Linux, check file permissions: `ls -la labXX/`

---

## 🦀 Rust-Specific Issues

### **Problem: "cargo: command not found"**
- **Cause**: Rust not installed or not in PATH
- **Solution**:
  - Install Rust: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
  - Restart your terminal
  - Verify: `cargo --version`
  - See [../resources/SETUP_GUIDE.md](./SETUP_GUIDE.md#5-rust) for detailed installation

### **Problem: "error: could not compile" with Rust**
- **Cause**: Syntax errors or type mismatches
- **Solution**:
  - Read the error message carefully - Rust errors are very descriptive
  - Check that all variables have correct types
  - Make sure functions return the expected type
  - Use `cargo check` for faster error checking without building

### **Problem: "test result: FAILED" with cargo test**
- **Cause**: Your implementation doesn't match test expectations
- **Solution**:
  - Read test output carefully - shows which assertion failed
  - Test functions manually to understand expected behavior
  - Check function signatures match exactly (parameter types, return type)
  - Use `println!()` statements to debug (won't show in passing tests)

---

## 🔍 Git and GitHub Issues

### **Problem: "Permission denied (publickey)" when pushing**
- **Cause**: SSH key not set up or PAT not configured
- **Solution**:
  - If using PAT: Make sure you're using HTTPS URL and PAT as password
  - Verify remote URL: `git remote -v`
  - Should be `https://github.com/username/repo.git` for PAT
  - See Lab 01 for PAT setup instructions

### **Problem: "refusing to merge unrelated histories"**
- **Cause**: Local and remote repositories have different histories
- **Solution**:
  - Usually safe to force: `git pull origin main --allow-unrelated-histories`
  - Or start fresh by re-cloning the repository

### **Problem: "Changes not showing on GitHub"**
- **Cause**: Forgot to push after committing
- **Solution**:
  - Commit: `git add . && git commit -m "message"`
  - Push: `git push origin main`
  - Verify on GitHub web interface that files updated

---

## 💻 Environment Issues

### **Problem: "Virtual environment not activating"**
- **Cause**: Wrong command for your OS or environment not created
- **Solution**:
  - Create first: `python -m venv venv`
  - Then activate:
    - macOS/Linux: `source venv/bin/activate`
    - Windows (Git Bash): `source venv/Scripts/activate`
    - Windows (Command Prompt): `venv\Scripts\activate.bat`
    - Windows (PowerShell): `venv\Scripts\Activate.ps1`
  - You should see `(venv)` in your terminal prompt

### **Problem: "python: command not found" or "python3: command not found"**
- **Cause**: Python not installed or not in PATH
- **Solution**:
  - Try both `python --version` and `python3 --version`
  - On macOS/Linux, you might need to use `python3`
  - Install Python if needed - see [SETUP_GUIDE.md](./SETUP_GUIDE.md#4-python)
  - On Windows, verify "Add to PATH" was checked during installation

---

## 🤖 AI Assistance Tips

When troubleshooting with AI tools (ChatGPT, Claude, Gemini):

**✅ Good prompts:**
- "I'm getting this error: [exact error message]. Here's my code: [paste code]. What's wrong?"
- "My function should return X but it returns Y. Here's my code: [paste code]"
- "How do I fix this pytest error: [error message]?"

**❌ Avoid:**
- "My code doesn't work" (too vague)
- Asking AI to write the entire solution without understanding
- Not including the actual error message

**Remember:**
- Always understand AI-generated solutions before using them
- Test AI suggestions to verify they work
- AI can make mistakes - verify against lab requirements

---

## 📚 Additional Resources

- **Python Documentation**: https://docs.python.org/3/
- **pytest Documentation**: https://docs.pytest.org/
- **Rust Documentation**: https://doc.rust-lang.org/
- **Git Documentation**: https://git-scm.com/doc
- **GitHub Actions**: https://docs.github.com/en/actions
- **Setup Guide**: [SETUP_GUIDE.md](./SETUP_GUIDE.md)

---

**Still stuck?**
- Review the specific lab's README for lab-specific troubleshooting
- Check the course discussion board (Microsoft Teams)
- Attend office hours
- Email the instructor with:
  - Exact error message
  - What you've tried
  - Screenshots if helpful
