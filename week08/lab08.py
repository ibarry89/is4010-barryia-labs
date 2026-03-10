"""Week 08 Weather CLI application."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional, Sequence

from favorites import FavoritesManager
from weather_api import (
    DEFAULT_BASE_URL,
    WeatherAPI,
    format_current_weather,
    format_forecast,
)

DEFAULT_FAVORITES_FILE = Path(__file__).with_name("favorites.json")
PLACEHOLDER_API_KEY = "YOUR_API_KEY_HERE"


def load_api_key() -> Optional[str]:
    """Load the weather API key from environment variables or config.py."""
    api_key = os.getenv("WEATHER_API_KEY")
    if api_key and api_key != PLACEHOLDER_API_KEY:
        return api_key

    try:
        from config import WEATHER_API_KEY  # type: ignore
    except ImportError:
        return None

    return WEATHER_API_KEY if WEATHER_API_KEY != PLACEHOLDER_API_KEY else None


def load_base_url() -> str:
    """Load the API base URL from config.py when available."""
    try:
        from config import WEATHER_API_BASE_URL  # type: ignore
    except ImportError:
        return DEFAULT_BASE_URL
    return WEATHER_API_BASE_URL


def resolve_location(location: str, favorites_manager: FavoritesManager) -> str:
    """Return the saved favorite location when one matches the input name."""
    return favorites_manager.get_location(location) or location


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Weather CLI application for current conditions and forecasts.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    current_parser = subparsers.add_parser(
        "current", help="Show current weather for a location or favorite name."
    )
    current_parser.add_argument("location", help="City, region, or favorite name.")
    current_parser.set_defaults(handler=handle_current)

    forecast_parser = subparsers.add_parser(
        "forecast", help="Show a 1-3 day forecast for a location or favorite name."
    )
    forecast_parser.add_argument("location", help="City, region, or favorite name.")
    forecast_parser.add_argument(
        "--days",
        type=int,
        choices=(1, 2, 3),
        default=3,
        help="Number of forecast days to display (1-3).",
    )
    forecast_parser.set_defaults(handler=handle_forecast)

    favorites_parser = subparsers.add_parser(
        "favorites", help="Manage favorite weather locations."
    )
    favorites_subparsers = favorites_parser.add_subparsers(
        dest="favorites_command", required=True
    )

    favorites_add_parser = favorites_subparsers.add_parser(
        "add", help="Add a named favorite location."
    )
    favorites_add_parser.add_argument("name", help="Favorite name.")
    favorites_add_parser.add_argument("location", help="Weather lookup location.")
    favorites_add_parser.set_defaults(handler=handle_favorites_add)

    favorites_list_parser = favorites_subparsers.add_parser(
        "list", help="List saved favorite locations."
    )
    favorites_list_parser.set_defaults(handler=handle_favorites_list)

    favorites_remove_parser = favorites_subparsers.add_parser(
        "remove", help="Remove a favorite location by name."
    )
    favorites_remove_parser.add_argument("name", help="Favorite name to remove.")
    favorites_remove_parser.set_defaults(handler=handle_favorites_remove)

    return parser


def build_weather_api() -> Optional[WeatherAPI]:
    """Create a WeatherAPI client when an API key is available."""
    api_key = load_api_key()
    if not api_key:
        return None
    return WeatherAPI(api_key=api_key, base_url=load_base_url())


def handle_current(args: argparse.Namespace, favorites_manager: FavoritesManager) -> int:
    """Handle the current weather command."""
    weather_api = build_weather_api()
    if weather_api is None:
        print(
            "Weather API key not configured. Set WEATHER_API_KEY or create week08/config.py."
        )
        return 1

    location = resolve_location(args.location, favorites_manager)
    data = weather_api.get_current_weather(location)
    if data is None:
        print(f"Unable to retrieve current weather for '{location}'.")
        return 1

    print(format_current_weather(data))
    return 0


def handle_forecast(args: argparse.Namespace, favorites_manager: FavoritesManager) -> int:
    """Handle the forecast command."""
    weather_api = build_weather_api()
    if weather_api is None:
        print(
            "Weather API key not configured. Set WEATHER_API_KEY or create week08/config.py."
        )
        return 1

    location = resolve_location(args.location, favorites_manager)
    data = weather_api.get_forecast(location, days=args.days)
    if data is None:
        print(f"Unable to retrieve forecast for '{location}'.")
        return 1

    print(format_forecast(data))
    return 0


def handle_favorites_add(
    args: argparse.Namespace, favorites_manager: FavoritesManager
) -> int:
    """Handle adding a favorite location."""
    if favorites_manager.add(args.name, args.location):
        print(f"Added favorite '{args.name}' for '{args.location}'.")
        return 0

    print(f"Favorite '{args.name}' already exists.")
    return 1


def handle_favorites_list(
    args: argparse.Namespace, favorites_manager: FavoritesManager
) -> int:
    """Handle listing all favorites."""
    favorites = favorites_manager.list_all()
    if not favorites:
        print("No favorites saved.")
        return 0

    for name, location in sorted(favorites.items()):
        print(f"{name}: {location}")
    return 0


def handle_favorites_remove(
    args: argparse.Namespace, favorites_manager: FavoritesManager
) -> int:
    """Handle removing a favorite location."""
    if favorites_manager.remove(args.name):
        print(f"Removed favorite '{args.name}'.")
        return 0

    print(f"Favorite '{args.name}' was not found.")
    return 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the weather CLI application."""
    parser = create_parser()
    args = parser.parse_args(argv)
    favorites_manager = FavoritesManager(DEFAULT_FAVORITES_FILE)
    return args.handler(args, favorites_manager)


__all__ = [
    "FavoritesManager",
    "WeatherAPI",
    "create_parser",
    "format_current_weather",
    "format_forecast",
    "load_api_key",
    "main",
    "resolve_location",
]


if __name__ == "__main__":
    raise SystemExit(main())
