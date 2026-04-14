from __future__ import annotations

import argparse
import sys
from pathlib import Path

from app.storage import append_entry, load_entries
from app.tracker import create_entry, filter_entries, summarize_entries


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="budget-buddy",
        description="Track personal expenses from the command line.",
    )
    parser.add_argument(
        "--file",
        default="expenses.json",
        help="Path to the JSON storage file (default: expenses.json)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--category", required=True, help="Expense category")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    add_parser.add_argument("--note", default="", help="Optional note")
    add_parser.add_argument("--date", default=None, help="Date in YYYY-MM-DD format")

    list_parser = subparsers.add_parser("list", help="List expenses")
    list_parser.add_argument("--category", default=None, help="Filter by category")
    list_parser.add_argument("--month", default=None, help="Filter by month (YYYY-MM)")

    summary_parser = subparsers.add_parser("summary", help="Show summary totals")
    summary_parser.add_argument("--month", default=None, help="Filter by month (YYYY-MM)")

    return parser


def command_add(args: argparse.Namespace) -> int:
    entry = create_entry(
        category=args.category,
        amount=args.amount,
        note=args.note,
        date_text=args.date,
    )
    append_entry(args.file, entry)
    print(
        f"Added ${entry['amount']:.2f} in {entry['category']} on {entry['date']}"
    )
    return 0


def command_list(args: argparse.Namespace) -> int:
    entries = load_entries(args.file)
    filtered = filter_entries(entries, category=args.category, month=args.month)

    if not filtered:
        print("No expenses found.")
        return 0

    print("Date       | Category   | Amount   | Note")
    print("-" * 50)
    for entry in filtered:
        print(
            f"{entry['date']} | {str(entry['category']):10} | ${float(entry['amount']):7.2f} | {entry['note']}"
        )
    return 0


def command_summary(args: argparse.Namespace) -> int:
    entries = load_entries(args.file)
    filtered = filter_entries(entries, month=args.month)
    summary = summarize_entries(filtered)

    print(f"Entries: {summary['count']}")
    print(f"Total: ${summary['overall_total']:.2f}")
    print("By category:")
    category_totals = summary["category_totals"]
    if not category_totals:
        print("  (none)")
        return 0

    for category, total in category_totals.items():
        print(f"  - {category}: ${total:.2f}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            return command_add(args)
        if args.command == "list":
            return command_list(args)
        if args.command == "summary":
            return command_summary(args)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print("Unknown command", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
