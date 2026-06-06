import unittest

import pandas as pd

import taichi_global_bathymetry as tgb


class DataFrameNormalizerFixtureParityTests(unittest.TestCase):
    def test_ais_empty_input_returns_expected_schema(self):
        out = tgb.normalize_ais_frame(pd.DataFrame())

        self.assertEqual(list(out.columns), ["lon", "lat", "mmsi", "sog", "cog", "heading", "timestamp"])
        self.assertTrue(out.empty)

    def test_ais_canonical_lat_lon_rows_are_retained(self):
        out = tgb.normalize_ais_frame(pd.DataFrame({"lat": [25.0], "lon": [121.0]}))

        self.assertEqual(len(out), 1)
        self.assertEqual(float(out.loc[0, "lat"]), 25.0)
        self.assertEqual(float(out.loc[0, "lon"]), 121.0)

    def test_ais_alias_coordinate_columns_normalize_to_lat_lon(self):
        out = tgb.normalize_ais_frame(pd.DataFrame({"latitude": ["24.5"], "longitude": ["120.5"]}))

        self.assertEqual(float(out.loc[0, "lat"]), 24.5)
        self.assertEqual(float(out.loc[0, "lon"]), 120.5)

    def test_ais_missing_coordinate_fields_raise(self):
        with self.assertRaises(ValueError):
            tgb.normalize_ais_frame(pd.DataFrame({"lat": [25.0], "mmsi": [1]}))

        with self.assertRaises(ValueError):
            tgb.normalize_ais_frame(pd.DataFrame({"lon": [121.0], "mmsi": [1]}))

    def test_ais_null_or_nonnumeric_coordinate_rows_are_dropped(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0, None, "not-number"],
                "lon": [121.0, 120.0, 119.0],
            }
        )

        out = tgb.normalize_ais_frame(frame)

        self.assertEqual(len(out), 1)
        self.assertEqual(float(out.loc[0, "lat"]), 25.0)

    def test_ais_latitude_bounds_and_longitude_wrapping_are_pinned(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0, 91.0, -91.0],
                "lon": [181.0, 121.0, -181.0],
            }
        )

        out = tgb.normalize_ais_frame(frame)

        self.assertEqual(len(out), 1)
        self.assertEqual(float(out.loc[0, "lat"]), 25.0)
        self.assertEqual(float(out.loc[0, "lon"]), -179.0)

    def test_ais_optional_columns_are_copied_and_numeric_columns_coerced(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0],
                "lon": [121.0],
                "MMSI": ["001234567"],
                "speed": ["12.5"],
                "course": ["180.5"],
                "HDG": ["181"],
                "received_at": ["2026-06-07T00:00:00Z"],
                "ship_name": ["Fixture Vessel"],
            }
        )

        out = tgb.normalize_ais_frame(frame)

        self.assertEqual(out.loc[0, "mmsi"], "001234567")
        self.assertEqual(float(out.loc[0, "sog"]), 12.5)
        self.assertEqual(float(out.loc[0, "cog"]), 180.5)
        self.assertEqual(float(out.loc[0, "heading"]), 181.0)
        self.assertEqual(out.loc[0, "timestamp"], "2026-06-07T00:00:00Z")
        self.assertEqual(out.loc[0, "name"], "Fixture Vessel")

    def test_aircraft_empty_input_returns_expected_schema(self):
        out = tgb.normalize_aircraft_frame(pd.DataFrame())

        self.assertEqual(
            list(out.columns),
            ["lon", "lat", "icao24", "callsign", "altitude_m", "speed_kt", "heading", "timestamp"],
        )
        self.assertTrue(out.empty)

    def test_aircraft_canonical_lat_lon_rows_are_retained(self):
        out = tgb.normalize_aircraft_frame(pd.DataFrame({"lat": [25.0], "lon": [121.0]}))

        self.assertEqual(len(out), 1)
        self.assertEqual(float(out.loc[0, "lat"]), 25.0)
        self.assertEqual(float(out.loc[0, "lon"]), 121.0)

    def test_aircraft_alias_coordinate_columns_normalize_to_lat_lon(self):
        out = tgb.normalize_aircraft_frame(pd.DataFrame({"position.lat": ["24.0"], "position.lon": ["120.0"]}))

        self.assertEqual(float(out.loc[0, "lat"]), 24.0)
        self.assertEqual(float(out.loc[0, "lon"]), 120.0)

    def test_aircraft_missing_coordinate_fields_raise(self):
        with self.assertRaises(ValueError):
            tgb.normalize_aircraft_frame(pd.DataFrame({"lat": [25.0], "icao24": ["abc"]}))

        with self.assertRaises(ValueError):
            tgb.normalize_aircraft_frame(pd.DataFrame({"lon": [121.0], "icao24": ["abc"]}))

    def test_aircraft_null_or_nonnumeric_coordinate_rows_are_dropped(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0, None, "bad"],
                "lon": [121.0, 120.0, 119.0],
            }
        )

        out = tgb.normalize_aircraft_frame(frame)

        self.assertEqual(len(out), 1)
        self.assertEqual(float(out.loc[0, "lat"]), 25.0)

    def test_aircraft_identity_heading_and_timestamp_aliases_are_copied(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0],
                "lon": [121.0],
                "hex": ["abc123"],
                "flight": ["RRK1"],
                "track": ["270"],
                "last_contact": ["2026-06-07T00:00:00Z"],
            }
        )

        out = tgb.normalize_aircraft_frame(frame)

        self.assertEqual(out.loc[0, "icao24"], "abc123")
        self.assertEqual(out.loc[0, "callsign"], "RRK1")
        self.assertEqual(float(out.loc[0, "heading"]), 270.0)
        self.assertEqual(out.loc[0, "timestamp"], "2026-06-07T00:00:00Z")

    def test_aircraft_altitude_m_and_speed_kt_sources_are_coerced(self):
        frame = pd.DataFrame(
            {
                "lat": [25.0],
                "lon": [121.0],
                "alt_m": ["1000.5"],
                "groundspeed": ["240.25"],
            }
        )

        out = tgb.normalize_aircraft_frame(frame)

        self.assertEqual(float(out.loc[0, "altitude_m"]), 1000.5)
        self.assertEqual(float(out.loc[0, "speed_kt"]), 240.25)

    def test_aircraft_altitude_ft_derives_altitude_m_and_remains_in_output(self):
        frame = pd.DataFrame({"lat": [25.0], "lon": [121.0], "altitude_ft": ["10000"]})

        out = tgb.normalize_aircraft_frame(frame)

        self.assertIn("altitude_ft", out.columns)
        self.assertEqual(float(out.loc[0, "altitude_ft"]), 10000.0)
        self.assertAlmostEqual(float(out.loc[0, "altitude_m"]), 3048.0)

    def test_aircraft_speed_ms_derives_speed_kt_and_remains_in_output(self):
        frame = pd.DataFrame({"lat": [25.0], "lon": [121.0], "velocity": ["100"]})

        out = tgb.normalize_aircraft_frame(frame)

        self.assertIn("speed_ms", out.columns)
        self.assertEqual(float(out.loc[0, "speed_ms"]), 100.0)
        self.assertAlmostEqual(float(out.loc[0, "speed_kt"]), 194.3844)

    def test_aircraft_missing_altitude_and_speed_defaults_are_pinned(self):
        out = tgb.normalize_aircraft_frame(pd.DataFrame({"lat": [25.0], "lon": [121.0]}))

        self.assertEqual(float(out.loc[0, "altitude_m"]), 0.0)
        self.assertTrue(pd.isna(out.loc[0, "speed_kt"]))

    def test_find_column_normalized_name_collision_uses_last_column(self):
        frame = pd.DataFrame({"lat": [1.0], "LAT": [2.0], "lon": [121.0]})

        found = tgb.find_column(frame, tgb.LAT_ALIASES)

        self.assertEqual(found, "LAT")
        out = tgb.normalize_ais_frame(frame)
        self.assertEqual(float(out.loc[0, "lat"]), 2.0)


if __name__ == "__main__":
    unittest.main()
