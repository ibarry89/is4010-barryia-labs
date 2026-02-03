# Week 00: Setup verification

**Due**: Not graded (optional setup verification)
**Points**: 0 (testing only)

## Overview

This is a **test lab** to verify your development environment and GitHub Actions CI/CD setup are working correctly. Complete this lab to ensure everything is configured properly before starting the actual course labs.

## Purpose

Week 00 helps you verify:
- ✅ Python environment works
- ✅ Rust toolchain works
- ✅ pytest is installed
- ✅ cargo test runs
- ✅ GitHub Actions CI/CD triggers correctly
- ✅ You understand the weekly workflow

**This lab contains NO actual course content** - it's purely for setup verification.

## Materials

- 📋 **Lab instructions**: [lab00.md](./lab00.md)
- 🧪 **Python test**: `tests/test_lab00.py` (provided)
- 🦀 **Rust test**: `week00_rust/` (optional Rust verification)

## Quick start - Python verification

1. **Read the instructions**: [lab00.md](./lab00.md)
2. **Create your solution**: Create `lab00.py` with a simple function
3. **Run tests locally**:

```bash
cd week00/
pytest tests/ -v

# Expected output:
# tests/test_lab00.py::test_hello_world PASSED
# tests/test_lab00.py::test_add_numbers PASSED
# ======================== 2 passed ========================
```

4. **Commit and push**:

```bash
git add week00/
git commit -m "Complete Week 00 setup verification"
git push origin main
```

5. **Verify CI/CD**: Check GitHub Actions shows green ✅

## Quick start - Rust verification (optional)

```bash
cd week00_rust/
cargo test
cargo clippy
```

## Expected repository structure

After completing this verification:

```
is4010-[your-username]-course/
├── week00/
│   ├── README.md         # This file
│   ├── lab00.md          # Simple instructions
│   ├── lab00.py          # Your solution ✅
│   └── tests/
│       └── test_lab00.py # Provided tests
├── week00_rust/          # Optional Rust verification
│   ├── Cargo.toml
│   └── src/
│       └── main.rs
└── README.md
```

## What this proves

If both tests pass:
- ✅ Your Python environment is correctly configured
- ✅ pytest is installed and working
- ✅ GitHub Actions can run your tests
- ✅ You understand the commit/push/verify workflow
- ✅ (Optional) Rust toolchain is working

**Once this passes, you're ready for Week 01!**

## Troubleshooting

**Tests fail locally?**
- Check that you created `lab00.py` (not `Lab00.py` or `lab0.py`)
- Make sure functions are named exactly: `hello_world()` and `add_numbers(a, b)`
- Run `python lab00.py` to check for syntax errors

**GitHub Actions failing?**
- Verify all files are committed: `git status`
- Check the Actions tab for error messages
- Make sure you pushed: `git push origin main`

## Need help?

1. Read [lab00.md](./lab00.md) - it's very simple
2. Check [SETUP_GUIDE.md](../resources/SETUP_GUIDE.md) for installation help
3. This is just testing - the actual labs start at Week 01
