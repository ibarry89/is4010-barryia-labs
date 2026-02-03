# AI Agent Instructions for IS4010 Course Repository

Student-facing template repository for IS4010: Python (weeks 0-8) + Rust (weeks 9-14) with automated GitHub Actions grading.

**Sister repository**: Instructor materials (slides, solutions, grading scripts) in separate private repo.

## Repository Structure

```
is4010-course/
├── week00-week14/          # Weekly lab directories
│   ├── lab*.md             # Lab instructions
│   ├── tests/              # pytest (weeks 3-8) or Rust tests (weeks 9-14)
│   └── notebook.ipynb      # Interactive Jupyter notebooks
├── resources/
│   ├── SETUP_GUIDE.md      # Tool installation guide
│   └── TROUBLESHOOTING.md  # Common issues
├── .github/workflows/      # CI/CD (one per week)
└── requirements.txt        # Python dependencies
```

**Key concepts**:
- Self-contained weeks (students work one at a time)
- Tests auto-run on push via GitHub Actions
- Weeks 0-2: Setup; 3-8: Python/pytest; 9-14: Rust/cargo

## Build & Test Commands

### Python (Weeks 0-8)
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux; Windows: source venv/Scripts/activate
pip install -r requirements.txt
pytest week03/tests/ -v
```

### Rust (Weeks 9-14)
```bash
cd week09
cargo test --verbose
cargo fmt --check
cargo clippy -- -D warnings
```

### GitHub Actions
- One workflow per week: `.github/workflows/week*.yml`
- Missing files = RED (exit 1), passing tests = GREEN (exit 0)
- Status badges in README show pass/fail

## Code Style & Conventions

### Python
- PEP 8, Python 3.10+, NumPy-style docstrings
- pytest with clear test names

### Rust
- Follow `rustfmt` and `clippy` (`-D warnings`)

### Markdown
- Sentence case, proper names (GitHub, VS Code, Python, Rust)
- Descriptive link anchors, 15+ links to official docs per lab
- Code blocks with language specified

## Lab Structure Standards

Every lab includes:
1. Header: Due date, points, learning objectives with hyperlinks
2. Background: Context, real-world applications
3. Prerequisites: Required setup/tools
4. Instructions: Step-by-step with examples
5. Expected Repository Structure: Cumulative tree
6. Testing (Labs 3+): pytest or cargo test
7. Troubleshooting (Labs 4+): 10+ common issues
8. Submission: Git commands, checklist

## Testing Requirements

### Python (Weeks 3-8)
- Files: `week*/tests/test_lab*.py`
- Import: `from lab03 import function_name`
- Add `export PYTHONPATH="${PYTHONPATH}:week03"` before pytest
- Mock with `unittest.mock.patch` for input/print/random

### Rust (Weeks 9-14)
- Tests in `src/main.rs` or `tests/`
- Must pass: `cargo test`, `cargo fmt --check`, `cargo clippy -- -D warnings`

## GitHub Actions Pattern

```yaml
on:
  workflow_dispatch:
  push:
    paths: ['week*/**', '.github/workflows/week*.yml']

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - Check if lab file exists
      - Run tests if exists (exit 0 = pass)
      - Fail if missing (exit 1 = red badge)
```

## Python Tooling

**Required**: Python 3.10+ from python.org, venv, pip

**Optional**: `uv` (instructor demos only, documented in SETUP_GUIDE)

**Common issues**:
- `ensurepip` error: See lab01.md troubleshooting
- Use `python3`/`pip3` before venv, `python`/`pip` after activation

## Security & Academic Integrity

- **NEVER** commit API keys, tokens, credentials
- `.gitignore` excludes `venv/`, `.env`
- AI tools encouraged but students must understand/document usage

## Contributing Guidelines

### Creating/Updating Labs
1. Analyze existing patterns first
2. Read SETUP_GUIDE.md for standards
3. Test all code examples
4. Add directory structure section
5. Include testing (Labs 3+)
6. Cross-reference resources
7. Verify all links

### Commit Messages
```bash
# Good
git commit -m "Add Lab 05 with dictionary exercises"
git commit -m "Fix week03 workflow missing file handling"

# Multi-line with context
git commit -m "Update week01 workflow to verify hello.py

- Check if week01/hello.py exists
- Run program if found
- Fail with message if missing"
```

## Development Tips

### Finding Things
- Labs: `week*/lab*.md`
- Tests: `week*/tests/` (Python) or `week*/src/` (Rust)
- Workflows: `.github/workflows/week*.yml`
- Resources: `resources/SETUP_GUIDE.md`, `resources/TROUBLESHOOTING.md`

### Quick Checks
```bash
ls .github/workflows/          # Verify workflows
pytest week03/tests/ -v        # Python tests
cd week09 && cargo test        # Rust tests
grep -r "topic" week*/lab*.md  # Find references
```

## Quick Reference

- **Versions**: Python 3.10+, Rust latest stable
- **Testing**: pytest (Python), cargo test (Rust)
- **CI/CD**: GitHub Actions (one per week)
- **Style**: Sentence case, descriptive links, code examples with language tags
