# Budget Buddy CLI

Budget Buddy CLI is a lightweight command-line expense tracker for students and early professionals who want a fast way to log spending without opening a spreadsheet. It stores data in a local JSON file and gives immediate summaries by month and category, so you can quickly see where your money is going.

The tool solves a common problem: finance apps can be slow or distracting when you only need quick logging and reporting. Budget Buddy keeps your workflow simple and scriptable while still providing useful analysis.

## Installation

1. Clone your repository and move into the project directory.
2. Create and activate a virtual environment.
3. Install dependencies.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

Run the CLI with:

```bash
python -m app.main --file expenses.json <command> [options]
```

Available commands:
- `add` adds a new expense entry.
- `list` displays matching expense entries.
- `summary` shows totals and category breakdown.

## Examples

### 1) Add an expense

```bash
python -m app.main --file expenses.json add --category food --amount 12.50 --note "Lunch"
```

Expected output:

```text
Added $12.50 in food on 2026-04-13
```

### 2) List April food expenses

```bash
python -m app.main --file expenses.json list --category food --month 2026-04
```

Expected output (sample):

```text
Date       | Category   | Amount   | Note
--------------------------------------------------
2026-04-13 | food       | $  12.50 | Lunch
2026-04-14 | food       | $   8.25 | Coffee and bagel
```

### 3) Show a monthly summary

```bash
python -m app.main --file expenses.json summary --month 2026-04
```

Expected output (sample):

```text
Entries: 4
Total: $64.75
By category:
  - food: $20.75
  - transport: $24.00
  - books: $20.00
```

## Testing

Run all tests:

```bash
pytest -v
```

The project includes six tests that cover:
- Entry validation and normalization
- Filtering behavior by category/month
- Summary calculations
- Storage round-trip behavior
- Missing file handling

## CI/CD

A GitHub Actions workflow is included at `.github/workflows/ci.yml`.
On every push to `main`, it:
- Sets up Python
- Installs dependencies
- Runs the full pytest suite

## Known limitations and future ideas

- Data is stored in plain JSON and may become slow for very large histories.
- Currency is assumed to be USD.
- Future improvements: CSV export, budget alerts, recurring expense templates, and richer terminal formatting.
