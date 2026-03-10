# IS4010 Labs - Idrissa Barry

## Lab Status (Repository)

| Week | Status | Topic |
|------|--------|-------|
| 00 | ![Week 00](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week00.yml/badge.svg) | Setup Verification |
| 01 | ![Week 01](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week01.yml/badge.svg) | Development Toolkit Setup |
| 02 | ![Week 02](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week02.yml/badge.svg) | AI-Assisted Development |
| 03 | ![Week 03](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week03.yml/badge.svg) | Python basics, testing, and CI/CD setup |
| 04 | ![Week 04](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week04.yml/badge.svg) | Data Structures |
| 05 | ![Week 05](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week05.yml/badge.svg) | Functions and Error Handling |
| 06 | ![Week 06](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week06.yml/badge.svg) | Object-Oriented Programming |
| 07 | ![Week 07](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week07.yml/badge.svg) | Data and APIs |
| 08 | ![Week 08](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week08.yml/badge.svg?branch=main) | Python CLI Application (Integrative) |
| 09 | ![Week 09](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week09.yml/badge.svg) | Rust Basics |
| 10 | ![Week 10](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week10.yml/badge.svg) | Ownership and Borrowing |
| 11 | ![Week 11](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week11.yml/badge.svg) | Structuring Code and Data |
| 12 | ![Week 12](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week12.yml/badge.svg) | Generics and Traits |
| 13 | ![Week 13](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week13.yml/badge.svg) | Idiomatic Rust |
| 14 | ![Week 14](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/week14.yml/badge.svg) | Rust CLI Application (Integrative) |


This repository contains all lab assignments for **IS4010: AI-Enhanced Application Development** at the University of Cincinnati's Lindner College of Business.

## 📚 Course Information

- **Course**: IS4010 - AI-Enhanced Application Development
- **Instructor**: Brandon Greenwell
- **Semester**: Spring 2025
- **Institution**: University of Cincinnati, Lindner College of Business

## 🧪 Automated Testing

This repository uses **GitHub Actions** for continuous integration. The badge above shows the current status of all tests:
- ✅ **Green checkmark**: All tests passing
- ❌ **Red X**: Some tests failing

Tests automatically run on every push to ensure code quality and correctness.

## 📂 Repository Structure

```
is4010-barryia-labs/
├── .github/workflows/     # CI/CD automation
├── card-war-api-game/     # Separate Card War API project (Python + FastAPI)
├── week01/                # Development toolkit setup
├── week02/                # AI-assisted development
├── week03/                # Python basics and automated testing
├── week04/                # Data Structures
└── README.md              # This file
```

## 🧩 Top-Level Projects

- `card-war-api-game/`: Standalone Card War game project with a REST API (`FastAPI`) ![Card War API Game](https://github.com/ibarry89/is4010-barryia-labs/actions/workflows/card-war-api-game.yml/badge.svg)

## 🚀 Labs Completed

- [x] **Lab 01**: Development Toolkit Setup
- [x] **Lab 02**: AI-Assisted Development
- [x] **Lab 03**: Python basics, testing, and CI/CD setup
- [x] **Lab 04**: Data Structures

## 🛠️ Technologies Used

- **Python 3.10+**: Primary programming language
- **pytest**: Testing framework for automated test execution
- **GitHub Actions**: CI/CD pipeline for automated testing
- **Git/GitHub**: Version control and collaboration

## 📝 Notes

This repository demonstrates modern software development practices including:
- Version control with Git
- Automated testing with pytest
- Continuous Integration/Continuous Deployment (CI/CD)
- AI-assisted development workflows
- Professional documentation standards

---

**About this course**: IS4010 explores application development enhanced by AI tools, covering Python fundamentals, testing practices, and modern development workflows. Students learn to leverage AI assistants while building strong programming fundamentals.
```

### 5. Verify Rust Installation

```bash
# Check Rust toolchain
rustc --version
cargo --version

# Should show Rust 1.70+ and Cargo
```

## Getting Started: Week 00 (Setup Verification)

**Before starting the actual course labs**, complete Week 00 to verify your setup:

```bash
cd week00/
# Create lab00.py with two simple functions (see lab00.md)
pytest tests/ -v      # Run tests locally
git add week00/
git commit -m "Complete Week 00 setup verification"
git push origin main
# Check GitHub Actions for green checkmark ✅
```

**Week 00 is a test lab** - it contains no actual course content. It just verifies:
- ✅ Python and pytest work
- ✅ Rust toolchain works (optional)
- ✅ GitHub Actions CI/CD works
- ✅ You understand the workflow

Once Week 00 passes, you're ready for the real labs!

## Weekly Workflow

Each week, you'll complete a lab assignment:

1. **Read the week overview** in `weekXX/README.md`
2. **Read detailed instructions** in `weekXX/labXX.md`
3. **Write your code** following the lab instructions
4. **Run tests locally** to verify your solution (weeks 3+)
5. **Commit and push** your changes to GitHub
6. **Verify CI/CD** - Check that GitHub Actions shows a green checkmark

### Example: Completing Week 03 Lab

```bash
# Navigate to week folder
cd week03/

# Read overview and instructions
cat README.md      # Brief overview
cat lab03.md       # Detailed instructions

# Write your code
# - Create lab03.py with your solution
# - Tests are provided in tests/test_lab03.py

# Run tests locally
pytest tests/ -v

# Commit your work
git add week03/
git commit -m "Complete Week 03 lab"
git push origin main

# Check GitHub Actions
# - Go to your repository on GitHub
# - Click "Actions" tab
# - Verify "Week 03 - Python Basics" workflow shows green checkmark ✓
```

## CI/CD and Grading

Each lab has an automated GitHub Actions workflow that runs when you push code:

- **Python labs (3-8)**: Run `pytest` to verify your tests pass
- **Rust labs (9-14)**: Run `cargo test`, `cargo fmt --check`, and `cargo clippy`

**Grading is based on CI/CD status**:
- ✅ **Green checkmark** = Lab passes (full credit)
- ❌ **Red X** = Lab fails (no credit until fixed)

**You must verify your CI/CD passes before the lab deadline.**

## Lab Descriptions

### Week 00: Setup Verification (Not Graded)

| Week | Topic |
|------|-------|
| 00 | Setup Verification - Test Python & Rust CI/CD |

**Purpose**: Verify your environment works before starting actual labs. Contains trivially simple functions - just for testing!

### Python Track (Weeks 1-8)

| Lab | Chapter | Topic |
|-----|---------|-------|
| 01 | Ch 1 | Development Toolkit Setup |
| 02 | Ch 2 | AI-Assisted Development |
| 03 | Ch 3 | Python Basics + Testing Infrastructure |
| 04 | Ch 4 | Data Structures |
| 05 | Ch 5 | Functions and Error Handling |
| 06 | Ch 6 | Object-Oriented Programming |
| 07 | Ch 7 | Data and APIs |
| 08 | Ch 8 | Python CLI Application (Integrative) |

### Rust Track (Weeks 9-14)

| Lab | Chapter | Topic |
|-----|---------|-------|
| 09 | Ch 9 | Rust Basics |
| 10 | Ch 10 | Ownership and Borrowing |
| 11 | Ch 11 | Structuring Code and Data |
| 12 | Ch 12 | Generics and Traits |
| 13 | Ch 13 | Idiomatic Rust |
| 14 | Ch 14 | Rust CLI Application (Integrative) |

## Important Notes

### Independent Labs
Each lab is **self-contained** and **independent**:
- You don't copy code from previous labs
- Each lab starts fresh with new exercises
- Failing one lab doesn't affect the next lab
- You can redo/skip labs without cascade failures

### AI Assistance Policy
You are **encouraged** to use AI coding assistants:
- **GitHub Copilot** (in-editor suggestions)
- **Gemini CLI** (terminal assistance)
- **ChatGPT, Claude, etc.** (conversational help)

**Academic Integrity Requirements**:
- You must **understand** all code you submit
- Document AI assistance in `week02/` and throughout
- The goal is **learning**, not just completion

### Testing Requirements
Starting with Lab 03, all labs require automated tests:
- **Python**: Use `pytest` framework
- **Rust**: Use built-in `cargo test`
- Tests must pass locally **and** in GitHub Actions
- Aim for comprehensive test coverage

## Troubleshooting

### Python Issues

**Virtual environment not activating:**
```bash
# Ensure you're in the repository root
pwd  # Should show .../is4010-YOUR-USERNAME-course

# Recreate virtual environment
rm -rf venv
python -m venv venv
source venv/bin/activate  # macOS/Linux
source venv/Scripts/activate  # Windows Git Bash
```

**pytest not found:**
```bash
# Activate virtual environment first
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Rust Issues

**cargo command not found:**
```bash
# Install Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Restart terminal, then verify
rustc --version
cargo --version
```

**Cargo.lock errors:**
- Cargo.lock is in .gitignore - don't commit it
- Run `cargo clean` if you see lock file errors

### GitHub Actions Failing

**Check the workflow log:**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Click the failing workflow run
4. Read the error messages
5. Fix the issue locally
6. Commit and push again

**Common issues:**
- Tests failing locally → Fix tests first
- Import errors → Check file names and paths
- Syntax errors → Run code locally before pushing

## Resources

- **Course Materials**: `is4010-course-template/` repository
- **Textbook**: *From Script to System* (aiappdev book)
- **Setup Guide**: See `is4010-course-template/resources/SETUP_GUIDE.md`

## Getting Help

1. **Read the lab README** thoroughly
2. **Check the textbook chapter** corresponding to the lab
3. **Use AI assistants** for coding help (with understanding)
4. **Check CI/CD logs** for specific error messages
5. **Ask on course discussion board** (Microsoft Teams)
6. **Attend office hours** for instructor help

## License

Course materials © 2025 Brandon M. Greenwell, University of Cincinnati
