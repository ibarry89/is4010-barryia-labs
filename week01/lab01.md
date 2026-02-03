# Lab 01: Development toolkit setup

## Learning Objectives

By the end of this lab, you will be able to:

- Install and verify essential development tools: [Git](https://git-scm.com/), [Python](https://www.python.org/), [VS Code](https://code.visualstudio.com/), and the [Rust toolchain](https://www.rust-lang.org/)
- Navigate your filesystem using the [command line](https://en.wikipedia.org/wiki/Command-line_interface) with confidence
- Create your first [GitHub repository](https://docs.github.com/en/repositories) and understand the basics of [version control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- Set up authentication between your local machine and GitHub using [Personal Access Tokens](https://docs.github.com/n/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- Fork the IS4010 labs template repository and complete your first commit
- Verify your development environment is ready for the entire semester

---

## Background

Professional software development requires a modern toolkit that enables you to write code efficiently, track changes systematically, and collaborate with others seamlessly. This lab establishes the foundation for all future work in IS4010 by setting up your development environment with industry-standard tools.

The four essential tools you'll install are:

1. **The command line**: A text-based interface for controlling your computer with precision and power
2. **Git**: The version control system used by over 94% of professional developers
3. **GitHub**: The world's largest platform for hosting code and building developer portfolios
4. **VS Code**: A modern, extensible code editor with AI integration capabilities

### Key Concepts

- **Command line**: Text-based interface for executing commands directly on your operating system
- **Version control**: System for tracking changes to files over time, enabling collaboration and safe experimentation
- **Repository (repo)**: A project folder tracked by Git, containing all files and their complete history
- **Commit**: A snapshot of your project at a specific point in time
- **Fork**: Creating your own copy of someone else's repository
- **SSH key**: A cryptographic authentication method that's more secure than passwords

---

## Prerequisites

For this first lab, you need:

- [ ] A computer running **Windows 10+**, **macOS 10.14+**, or a recent **Linux distribution**
- [ ] Administrator access to install software
- [ ] A stable internet connection for downloading tools (~500 MB total)
- [ ] A personal email address (we recommend using your UC email for GitHub student benefits)
- [ ] Approximately **90-120 minutes** to complete all installation and setup steps

**Important for Windows users**: Follow the [Windows Terminal + Git Bash setup](../resources/SETUP_GUIDE.md#recommendations-for-windows-users) in the SETUP_GUIDE. This ensures consistency with macOS/Linux users.

---

## Instructions

### Part 1: Install required tools (45-60 minutes)

Install all required development tools by following the comprehensive [IS4010 SETUP_GUIDE.md](../resources/SETUP_GUIDE.md).

Complete these sections in order:

1. **[Section 1: Visual Studio Code](../resources/SETUP_GUIDE.md#1-visual-studio-code-vs-code)** - Install VS Code and verify with `code --version`
2. **[Section 2: Git](../resources/SETUP_GUIDE.md#2-git)** - Install Git and verify with `git --version`
3. **[Section 3: GitHub Account & Student Benefits](../resources/SETUP_GUIDE.md#3-github-account--student-benefits)** - Create account and apply for [GitHub Student Developer Pack](https://education.github.com/pack)
4. **[Section 4: Python](../resources/SETUP_GUIDE.md#4-python)** - Install Python 3.10+ and verify with `python --version` or `python3 --version`
5. **[Section 5: Rust](../resources/SETUP_GUIDE.md#5-rust)** - Install Rust toolchain and verify with `cargo --version`
6. **[Section 8: Recommended VS Code Extensions](../resources/SETUP_GUIDE.md#8-recommended-vs-code-extensions)** - Install Python, rust-analyzer, and other essential extensions

**Verification checkpoint**: After completing installations, verify all tools work:

```bash
# Check VS Code
code --version
# Check Git
git --version
# Check Python
python --version
# or python3 --version
# Check Rust
cargo --version
rustc --version
```

---

### Part 2: Configure Git identity (5 minutes)

Tell Git who you are so your commits are properly attributed.

```bash
# Set your name (use your real name)
git config --global user.name "Your Full Name"
# Set your email (use the same email as your GitHub account)
git config --global user.email "your-email@example.com"
# Verify configuration
git config --global --list
```

---

### Part 3: Set up GitHub authentication with Personal Access Token (10-15 minutes)

Follow the steps in the lab to generate a PAT with `repo` scope and store it securely. Use it as your password when Git prompts during `git push`.

---

### Part 4: Fork and clone the labs repository (10-15 minutes)

1. Fork the instructor's template repository
2. Add the instructor as a collaborator (bgreenwell)
3. Clone your fork locally

---

### Part 5: Set up Python virtual environment (10 minutes)

```bash
# Create virtual environment
python -m venv venv
# Activate virtual environment
# macOS/Linux: source venv/bin/activate
# Windows (Git Bash): source venv/Scripts/activate
# Install dependencies
pip install -r requirements.txt
```

---

### Part 6: Create your first Python program (10 minutes)

Create `hello.py` in `week01/` with the following content:

```python
"""
Lab 01: Development Toolkit Setup
Author: Your Name
Date: January 2025

This program demonstrates that your Python environment is correctly configured.
"""


def main():
    """Print a greeting and verify Python installation."""
    print("Hello, IS4010!")
    print("My development environment is ready.")

    import sys
    print(f"\nPython version: {sys.version}")
    print(f"Python executable: {sys.executable}")


if __name__ == "__main__":
    main()
```

---

### Part 7: Commit and push your work (10-15 minutes)

Stage, commit, and push your changes with a clear commit message and verify on GitHub.

---

## Success Criteria

- [ ] `hello.py` exists and runs
- [ ] Virtual environment created and `pytest` available
- [ ] Repository is private and instructor added as collaborator
- [ ] Completed steps verified and pushed to GitHub
