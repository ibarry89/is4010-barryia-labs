"""Favorites management for the Week 08 weather CLI."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional


class FavoritesManager:
    """Manage favorite locations with JSON persistence.

    Parameters
    ----------
    filename : str | Path, optional
        Path to the JSON file used for persistence.
    """

    def __init__(self, filename: str | Path = "favorites.json") -> None:
        self.filename = Path(filename)
        self._favorites: Dict[str, str] = {}
        self.load_favorites()

    @staticmethod
    def _normalize_name(name: str) -> str:
        """Return a normalized lookup key for a favorite name."""
        return name.strip().casefold()

    def load_favorites(self) -> Dict[str, str]:
        """Load favorites from disk.

        Returns
        -------
        dict
            The loaded favorites. Returns an empty dictionary if the file does
            not exist, contains invalid JSON, or has an invalid structure.
        """
        if not self.filename.exists():
            self._favorites = {}
            return {}

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError):
            self._favorites = {}
            return {}

        if not isinstance(data, dict):
            self._favorites = {}
            return {}

        cleaned: Dict[str, str] = {}
        for name, location in data.items():
            if isinstance(name, str) and isinstance(location, str):
                cleaned[name] = location

        self._favorites = cleaned
        return self.list_all()

    def save_favorites(self) -> None:
        """Save favorites to disk in formatted JSON."""
        if self.filename.parent != Path(""):
            self.filename.parent.mkdir(parents=True, exist_ok=True)

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self._favorites, file, indent=4, sort_keys=True)

    def add(self, name: str, location: str) -> bool:
        """Add a favorite location.

        Parameters
        ----------
        name : str
            The favorite name.
        location : str
            The location string for weather lookups.

        Returns
        -------
        bool
            True when the favorite was added, False if it already exists.
        """
        normalized_name = self._normalize_name(name)
        for existing_name in self._favorites:
            if self._normalize_name(existing_name) == normalized_name:
                return False

        self._favorites[name.strip()] = location.strip()
        self.save_favorites()
        return True

    def remove(self, name: str) -> bool:
        """Remove a favorite by name.

        Parameters
        ----------
        name : str
            The favorite name to remove.

        Returns
        -------
        bool
            True when removed, False if no favorite matched.
        """
        normalized_name = self._normalize_name(name)
        for existing_name in list(self._favorites):
            if self._normalize_name(existing_name) == normalized_name:
                del self._favorites[existing_name]
                self.save_favorites()
                return True
        return False

    def list_all(self) -> Dict[str, str]:
        """Return a copy of all favorites."""
        return dict(self._favorites)

    def get_location(self, name: str) -> Optional[str]:
        """Get a location by favorite name using a case-insensitive lookup."""
        normalized_name = self._normalize_name(name)
        for existing_name, location in self._favorites.items():
            if self._normalize_name(existing_name) == normalized_name:
                return location
        return None
