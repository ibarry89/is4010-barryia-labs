from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import date


@dataclass(frozen=True)
class ExpenseEntry:
    date: str
    category: str
    amount: float
    note: str


def parse_date(date_text: str) -> date:
    """Parse a YYYY-MM-DD string into a date object."""
    try:
        return date.fromisoformat(date_text)
    except ValueError as exc:
        raise ValueError("Date must be in YYYY-MM-DD format") from exc


def create_entry(category: str, amount: float, note: str = "", date_text: str | None = None) -> dict[str, str | float]:
    """Create a validated expense entry."""
    normalized_category = category.strip().lower()
    if not normalized_category:
        raise ValueError("Category cannot be empty")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if date_text is None:
        entry_date = date.today().isoformat()
    else:
        entry_date = parse_date(date_text).isoformat()

    entry = ExpenseEntry(
        date=entry_date,
        category=normalized_category,
        amount=round(float(amount), 2),
        note=note.strip(),
    )
    return asdict(entry)


def filter_entries(
    entries: list[dict[str, str | float]],
    *,
    category: str | None = None,
    month: str | None = None,
) -> list[dict[str, str | float]]:
    """Filter entries by category and/or month (YYYY-MM)."""
    filtered = entries

    if category:
        category_filter = category.strip().lower()
        filtered = [entry for entry in filtered if str(entry["category"]).lower() == category_filter]

    if month:
        if len(month) != 7 or month[4] != "-":
            raise ValueError("Month must be in YYYY-MM format")
        filtered = [entry for entry in filtered if str(entry["date"]).startswith(month)]

    return filtered


def summarize_entries(entries: list[dict[str, str | float]]) -> dict[str, object]:
    """Build totals for all entries and by category."""
    category_totals: dict[str, float] = defaultdict(float)
    overall_total = 0.0

    for entry in entries:
        amount = float(entry["amount"])
        category = str(entry["category"])
        category_totals[category] += amount
        overall_total += amount

    sorted_category_totals = {
        key: round(category_totals[key], 2)
        for key in sorted(category_totals)
    }

    return {
        "count": len(entries),
        "overall_total": round(overall_total, 2),
        "category_totals": sorted_category_totals,
    }
