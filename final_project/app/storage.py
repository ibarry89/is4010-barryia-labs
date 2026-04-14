from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_entries(file_path: str | Path) -> list[dict[str, Any]]:
    """Load expense entries from disk.

    Returns an empty list when the file does not exist.
    """
    path = Path(file_path)
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, list):
        raise ValueError("Storage file is corrupted: expected a list")

    return data


def save_entries(file_path: str | Path, entries: list[dict[str, Any]]) -> None:
    """Persist expense entries to disk as pretty JSON."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as handle:
        json.dump(entries, handle, indent=2)


def append_entry(file_path: str | Path, entry: dict[str, Any]) -> None:
    """Append one entry to storage."""
    entries = load_entries(file_path)
    entries.append(entry)
    save_entries(file_path, entries)
