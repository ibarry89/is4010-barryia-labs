# AGENTS.md

## How I used AI during development

I used AI as a coding partner to accelerate planning, code scaffolding, and test coverage.

### Where AI helped
- Brainstormed project ideas that were realistic for a solo capstone.
- Proposed a clean Python project structure with separate CLI, business logic, and storage modules.
- Drafted first-pass implementations for parsing, validation, filtering, and summary logic.
- Generated an initial pytest suite and a starter GitHub Actions workflow.
- Helped improve README clarity and examples.

### Where AI steered me wrong
- Suggested a few overly broad features at first, which would have made the project scope too large.
- Produced one early version of tests that focused too much on happy paths, so I added stronger edge-case checks.
- Initially used generic output text that was less helpful for users; I revised messages for clarity.

### What I learned
- Small, testable modules make it much easier to build a reliable CLI.
- Writing tests early exposes design issues quickly.
- AI suggestions are most useful when prompts are precise and when I review every line critically.
- I am responsible for understanding and verifying all final code.

## Verification steps I used
- Ran the test suite locally with `pytest -v`.
- Confirmed command behavior manually with sample CLI inputs.
- Added CI so tests run automatically on every push to `main`.
