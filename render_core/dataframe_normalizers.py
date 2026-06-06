from __future__ import annotations

import numpy as np
import pandas as pd


LAT_ALIASES = (
    "lat",
    "latitude",
    "y",
    "position.lat",
    "position.latitude",
    "navigation.lat",
    "ais.lat",
)
LON_ALIASES = (
    "lon",
    "lng",
    "long",
    "longitude",
    "x",
    "position.lon",
    "position.lng",
    "position.longitude",
    "navigation.lon",
    "ais.lon",
)
COLUMN_ALIASES = {
    "mmsi": ("mmsi", "MMSI", "ship_mmsi", "vessel_mmsi", "id"),
    "sog": ("sog", "SOG", "speed", "speed_knots", "speed_over_ground"),
    "cog": ("cog", "COG", "course", "course_over_ground"),
    "heading": ("heading", "true_heading", "hdg", "HDG"),
    "timestamp": (
        "timestamp",
        "time",
        "datetime",
        "received_at",
        "last_seen",
        "last_position_update",
    ),
    "name": ("name", "shipname", "vessel_name", "ship_name"),
}
AIRCRAFT_COLUMN_ALIASES = {
    "icao24": ("icao24", "icao", "hex", "hexident", "aircraft_id", "id"),
    "callsign": ("callsign", "call_sign", "flight", "flight_id", "ident"),
    "altitude_m": ("altitude_m", "alt_m", "baro_altitude", "geo_altitude", "altitude", "height_m"),
    "altitude_ft": ("altitude_ft", "alt_ft", "baro_altitude_ft", "geo_altitude_ft", "height_ft"),
    "speed_kt": ("speed_kt", "speed_knots", "groundspeed", "gs", "ground_speed_kt"),
    "speed_ms": ("speed_ms", "velocity", "ground_speed_ms", "speed_mps"),
    "heading": ("heading", "track", "true_track", "course"),
    "timestamp": ("timestamp", "time", "last_seen", "last_contact", "seen", "received_at"),
}


def normalize_name(name: object) -> str:
    return "".join(ch for ch in str(name).lower() if ch.isalnum())


def find_column(frame: pd.DataFrame, aliases: tuple[str, ...]) -> str | None:
    normalized = {normalize_name(col): col for col in frame.columns}
    for alias in aliases:
        found = normalized.get(normalize_name(alias))
        if found is not None:
            return found
    return None


def normalize_ais_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["lon", "lat", "mmsi", "sog", "cog", "heading", "timestamp"])

    lat_col = find_column(frame, LAT_ALIASES)
    lon_col = find_column(frame, LON_ALIASES)
    if lat_col is None or lon_col is None:
        raise ValueError(
            "AIS data must contain latitude/longitude columns. "
            f"Found columns: {', '.join(map(str, frame.columns[:20]))}"
        )

    out = pd.DataFrame(
        {
            "lat": pd.to_numeric(frame[lat_col], errors="coerce"),
            "lon": pd.to_numeric(frame[lon_col], errors="coerce"),
        }
    )
    for target, aliases in COLUMN_ALIASES.items():
        col = find_column(frame, aliases)
        if col is not None:
            out[target] = frame[col]

    for numeric_col in ("sog", "cog", "heading"):
        if numeric_col in out.columns:
            out[numeric_col] = pd.to_numeric(out[numeric_col], errors="coerce")

    out = out.dropna(subset=["lat", "lon"]).copy()
    out["lon"] = ((out["lon"] + 180.0) % 360.0) - 180.0
    out = out[out["lat"].between(-90.0, 90.0) & out["lon"].between(-180.0, 180.0)]
    return out.reset_index(drop=True)


def normalize_aircraft_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(columns=["lon", "lat", "icao24", "callsign", "altitude_m", "speed_kt", "heading", "timestamp"])

    lat_col = find_column(frame, LAT_ALIASES)
    lon_col = find_column(frame, LON_ALIASES)
    if lat_col is None or lon_col is None:
        raise ValueError(
            "ADS-B data must contain latitude/longitude columns. "
            f"Found columns: {', '.join(map(str, frame.columns[:20]))}"
        )
    out = pd.DataFrame(
        {
            "lat": pd.to_numeric(frame[lat_col], errors="coerce"),
            "lon": pd.to_numeric(frame[lon_col], errors="coerce"),
        }
    )
    for target, aliases in AIRCRAFT_COLUMN_ALIASES.items():
        col = find_column(frame, aliases)
        if col is not None:
            out[target] = frame[col]
    for numeric_col in ("altitude_m", "altitude_ft", "speed_kt", "speed_ms", "heading"):
        if numeric_col in out.columns:
            out[numeric_col] = pd.to_numeric(out[numeric_col], errors="coerce")
    if "altitude_m" not in out.columns and "altitude_ft" in out.columns:
        out["altitude_m"] = out["altitude_ft"] * 0.3048
    if "speed_kt" not in out.columns and "speed_ms" in out.columns:
        out["speed_kt"] = out["speed_ms"] * 1.943844
    if "altitude_m" not in out.columns:
        out["altitude_m"] = 0.0
    if "speed_kt" not in out.columns:
        out["speed_kt"] = np.nan
    out = out.dropna(subset=["lat", "lon"]).copy()
    out["lon"] = ((out["lon"] + 180.0) % 360.0) - 180.0
    out = out[out["lat"].between(-90.0, 90.0) & out["lon"].between(-180.0, 180.0)]
    return out.reset_index(drop=True)
