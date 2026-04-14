from app.tracker import create_entry, filter_entries, summarize_entries
from app.storage import append_entry, load_entries


def test_create_entry_normalizes_category_and_rounds_amount() -> None:
    entry = create_entry("  Food  ", 12.345, note="Lunch", date_text="2026-04-10")
    assert entry["category"] == "food"
    assert entry["amount"] == 12.35
    assert entry["date"] == "2026-04-10"


def test_create_entry_rejects_non_positive_amount() -> None:
    try:
        create_entry("food", 0)
        assert False, "Expected ValueError for zero amount"
    except ValueError as error:
        assert "greater than zero" in str(error)


def test_filter_entries_by_category_and_month() -> None:
    entries = [
        create_entry("food", 10, date_text="2026-04-01"),
        create_entry("travel", 50, date_text="2026-04-02"),
        create_entry("food", 30, date_text="2026-05-03"),
    ]

    filtered = filter_entries(entries, category="food", month="2026-04")
    assert len(filtered) == 1
    assert filtered[0]["amount"] == 10.0


def test_summarize_entries_returns_totals() -> None:
    entries = [
        create_entry("food", 10, date_text="2026-04-01"),
        create_entry("food", 15, date_text="2026-04-02"),
        create_entry("transport", 20, date_text="2026-04-03"),
    ]

    summary = summarize_entries(entries)
    assert summary["count"] == 3
    assert summary["overall_total"] == 45.0
    assert summary["category_totals"] == {"food": 25.0, "transport": 20.0}


def test_storage_append_and_load_round_trip(tmp_path) -> None:
    storage_file = tmp_path / "expenses.json"

    append_entry(storage_file, create_entry("food", 12, date_text="2026-04-10"))
    append_entry(storage_file, create_entry("books", 22, date_text="2026-04-11"))

    entries = load_entries(storage_file)
    assert len(entries) == 2
    assert entries[0]["category"] == "food"
    assert entries[1]["category"] == "books"


def test_load_entries_returns_empty_list_when_file_missing(tmp_path) -> None:
    storage_file = tmp_path / "missing.json"
    assert load_entries(storage_file) == []
