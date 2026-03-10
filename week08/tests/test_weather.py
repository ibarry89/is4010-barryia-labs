"""Tests for the Week 08 weather lab."""

from __future__ import annotations

from pathlib import Path

import pytest

from favorites import FavoritesManager


@pytest.fixture
def favorites_file(tmp_path: Path) -> Path:
    """Provide a temporary favorites file path."""
    return tmp_path / "favorites.json"


@pytest.fixture
def manager(favorites_file: Path) -> FavoritesManager:
    """Create a manager backed by a temporary file."""
    return FavoritesManager(favorites_file)


def test_add_favorite(manager: FavoritesManager) -> None:
    """Adding a new favorite should succeed."""
    assert manager.add("home", "Cincinnati, OH") is True
    assert manager.get_location("home") == "Cincinnati, OH"


def test_add_duplicate_favorite_returns_false(manager: FavoritesManager) -> None:
    """Adding the same favorite twice should fail."""
    assert manager.add("home", "Cincinnati, OH") is True
    assert manager.add("HOME", "Columbus, OH") is False


def test_remove_favorite(manager: FavoritesManager) -> None:
    """Removing an existing favorite should succeed."""
    manager.add("home", "Cincinnati, OH")
    assert manager.remove("home") is True
    assert manager.get_location("home") is None


def test_remove_missing_favorite_returns_false(manager: FavoritesManager) -> None:
    """Removing a missing favorite should fail cleanly."""
    assert manager.remove("missing") is False


def test_list_all_returns_saved_favorites(manager: FavoritesManager) -> None:
    """Listing favorites should return every stored entry."""
    manager.add("home", "Cincinnati, OH")
    manager.add("work", "Columbus, OH")

    assert manager.list_all() == {
        "home": "Cincinnati, OH",
        "work": "Columbus, OH",
    }


def test_get_location_is_case_insensitive(manager: FavoritesManager) -> None:
    """Favorite lookups should ignore case."""
    manager.add("Home", "Cincinnati, OH")
    assert manager.get_location("home") == "Cincinnati, OH"
    assert manager.get_location("HOME") == "Cincinnati, OH"


def test_persistence_across_instances(favorites_file: Path) -> None:
    """Favorites should persist when a new manager instance is created."""
    first_manager = FavoritesManager(favorites_file)
    first_manager.add("home", "Cincinnati, OH")

    second_manager = FavoritesManager(favorites_file)
    assert second_manager.get_location("home") == "Cincinnati, OH"
    assert second_manager.list_all() == {"home": "Cincinnati, OH"}


def test_corrupted_json_loads_as_empty(favorites_file: Path) -> None:
    """Corrupted JSON should not crash loading."""
    favorites_file.write_text("{not valid json", encoding="utf-8")

    manager = FavoritesManager(favorites_file)
    assert manager.list_all() == {}


def test_nonexistent_file_loads_as_empty(favorites_file: Path) -> None:
    """Missing files should load as empty favorites."""
    manager = FavoritesManager(favorites_file)
    assert manager.list_all() == {}


def test_saved_json_is_formatted(manager: FavoritesManager, favorites_file: Path) -> None:
    """Saved JSON should be indented for readability."""
    manager.add("home", "Cincinnati, OH")
    content = favorites_file.read_text(encoding="utf-8")

    assert "\n" in content
    assert "    " in content
