"""Weather API client and formatting helpers for the Week 08 lab."""

from __future__ import annotations

from typing import Any, Optional

import requests

DEFAULT_BASE_URL = "http://api.weatherapi.com/v1"


class WeatherAPI:
    """Simple client for WeatherAPI.com.

    Parameters
    ----------
    api_key : str
        API key for WeatherAPI.com.
    base_url : str, optional
        Base API URL.
    timeout : int, optional
        Request timeout in seconds.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = 10,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _get(self, endpoint: str, params: dict[str, Any]) -> Optional[dict[str, Any]]:
        """Send a GET request and return parsed JSON or None on error."""
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params={"key": self.api_key, **params},
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

        if isinstance(data, dict) and data.get("error"):
            return None
        return data if isinstance(data, dict) else None

    def get_current_weather(self, location: str) -> Optional[dict[str, Any]]:
        """Fetch current weather for a location."""
        return self._get("current.json", {"q": location, "aqi": "no"})

    def get_forecast(self, location: str, days: int = 3) -> Optional[dict[str, Any]]:
        """Fetch a forecast for a location."""
        safe_days = max(1, min(days, 3))
        return self._get(
            "forecast.json",
            {"q": location, "days": safe_days, "aqi": "no", "alerts": "yes"},
        )


def format_current_weather(data: Optional[dict[str, Any]]) -> str:
    """Format current weather data for CLI display."""
    if not data:
        return "Weather data is unavailable."

    location = data.get("location", {})
    current = data.get("current", {})
    condition = current.get("condition", {})
    location_name = location.get("name", "Unknown location")
    region = location.get("region") or location.get("country", "Unknown region")

    return "\n".join(
        [
            "=" * 50,
            f"Current Weather for {location_name}, {region}",
            "=" * 50,
            f"Condition: {condition.get('text', 'Unknown')}",
            (
                f"Temperature: {current.get('temp_f', 'N/A')}°F "
                f"({current.get('temp_c', 'N/A')}°C)"
            ),
            (
                f"Feels Like: {current.get('feelslike_f', 'N/A')}°F "
                f"({current.get('feelslike_c', 'N/A')}°C)"
            ),
            f"Humidity: {current.get('humidity', 'N/A')}%",
            f"Wind: {current.get('wind_mph', 'N/A')} mph {current.get('wind_dir', '')}".strip(),
            f"Last Updated: {current.get('last_updated', 'N/A')}",
            "=" * 50,
        ]
    )


def format_forecast(data: Optional[dict[str, Any]]) -> str:
    """Format forecast data for CLI display."""
    if not data:
        return "Forecast data is unavailable."

    location = data.get("location", {})
    forecast_days = data.get("forecast", {}).get("forecastday", [])
    location_name = location.get("name", "Unknown location")
    region = location.get("region") or location.get("country", "Unknown region")

    lines = ["=" * 50, f"Forecast for {location_name}, {region}", "=" * 50]
    if not forecast_days:
        lines.append("No forecast data available.")
    else:
        for day in forecast_days:
            date = day.get("date", "Unknown date")
            day_info = day.get("day", {})
            condition = day_info.get("condition", {})
            lines.extend(
                [
                    f"Date: {date}",
                    f"Condition: {condition.get('text', 'Unknown')}",
                    (
                        f"High/Low: {day_info.get('maxtemp_f', 'N/A')}°F / "
                        f"{day_info.get('mintemp_f', 'N/A')}°F"
                    ),
                    (
                        f"High/Low (C): {day_info.get('maxtemp_c', 'N/A')}°C / "
                        f"{day_info.get('mintemp_c', 'N/A')}°C"
                    ),
                    f"Chance of rain: {day_info.get('daily_chance_of_rain', 'N/A')}%",
                    "-" * 50,
                ]
            )

    if lines[-1] == "-" * 50:
        lines.pop()
    lines.append("=" * 50)
    return "\n".join(lines)
