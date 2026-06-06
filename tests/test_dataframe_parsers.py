import unittest
from unittest import mock

import pandas as pd

import taichi_global_bathymetry as tgb


class DataFrameParserFixtureParityTests(unittest.TestCase):
    def test_geojson_point_feature_adds_lon_lat(self):
        frame = tgb.dataframe_from_geojson(
            {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {"name": "alpha"},
                        "geometry": {"type": "Point", "coordinates": [121.5, 25.0]},
                    }
                ],
            }
        )

        self.assertEqual(list(frame["name"]), ["alpha"])
        self.assertEqual(float(frame.loc[0, "lon"]), 121.5)
        self.assertEqual(float(frame.loc[0, "lat"]), 25.0)

    def test_geojson_non_point_feature_preserves_properties(self):
        frame = tgb.dataframe_from_geojson(
            {
                "features": [
                    {
                        "properties": {"name": "line"},
                        "geometry": {"type": "LineString", "coordinates": [[0, 0], [1, 1]]},
                    }
                ]
            }
        )

        self.assertEqual(list(frame.columns), ["name"])
        self.assertEqual(frame.loc[0, "name"], "line")

    def test_json_feature_collection_delegates_to_geojson_behavior(self):
        frame = tgb.dataframe_from_json(
            '{"type":"FeatureCollection","features":[{"properties":{"id":7},"geometry":{"type":"Point","coordinates":[10,20]}}]}'
        )

        self.assertEqual(int(frame.loc[0, "id"]), 7)
        self.assertEqual(float(frame.loc[0, "lon"]), 10.0)
        self.assertEqual(float(frame.loc[0, "lat"]), 20.0)

    def test_json_opensky_states_maps_expected_column_prefix(self):
        frame = tgb.dataframe_from_json('{"states":[["abc123","CALL","TW",1,2,121.0,25.0]]}')

        self.assertEqual(
            list(frame.columns),
            ["icao24", "callsign", "origin_country", "time_position", "last_contact", "lon", "lat"],
        )
        self.assertEqual(frame.loc[0, "icao24"], "abc123")

    def test_json_known_list_key_normalizes_rows(self):
        frame = tgb.dataframe_from_json('{"ships":[{"mmsi":1,"nested":{"speed":12}}]}')

        self.assertIn("mmsi", frame.columns)
        self.assertIn("nested.speed", frame.columns)
        self.assertEqual(int(frame.loc[0, "mmsi"]), 1)

    def test_json_list_direct_normalize(self):
        frame = tgb.dataframe_from_json('[{"a":1},{"a":2}]')

        self.assertEqual(list(frame["a"]), [1, 2])

    def test_jsonl_ignores_blank_lines(self):
        frame = tgb.dataframe_from_jsonl('{"a":1}\n\n {"a":2}\n')

        self.assertEqual(list(frame["a"]), [1, 2])

    def test_invalid_jsonl_raises(self):
        with self.assertRaises(Exception):
            tgb.dataframe_from_jsonl('{"a":1}\nnot-json\n')

    def test_nmea_missing_decoder_path_returns_empty_dataframe(self):
        original_import = __import__

        def fake_import(name, *args, **kwargs):
            if name == "pyais":
                raise ImportError("fixture missing pyais")
            return original_import(name, *args, **kwargs)

        with mock.patch("builtins.__import__", side_effect=fake_import):
            frame = tgb.dataframe_from_nmea("!AIVDM,fixture")

        self.assertIsInstance(frame, pd.DataFrame)
        self.assertTrue(frame.empty)

    def test_dataframe_from_text_dispatches_geojson(self):
        frame = tgb.dataframe_from_text(
            '{"type":"FeatureCollection","features":[{"properties":{"id":1},"geometry":{"type":"Point","coordinates":[1,2]}}]}',
            "sample.geojson",
        )

        self.assertEqual(float(frame.loc[0, "lon"]), 1.0)
        self.assertEqual(float(frame.loc[0, "lat"]), 2.0)

    def test_dataframe_from_text_dispatches_jsonl(self):
        frame = tgb.dataframe_from_text('{"a":1}\n{"a":2}\n', "sample.jsonl")

        self.assertEqual(list(frame["a"]), [1, 2])

    def test_dataframe_from_text_dispatches_nmea_when_non_empty(self):
        expected = pd.DataFrame([{"lat": 25.0, "lon": 121.0}])

        with mock.patch.object(tgb, "dataframe_from_nmea", return_value=expected) as parser:
            frame = tgb.dataframe_from_text("!AIVDM,fixture", "sample.txt")

        parser.assert_called()
        self.assertEqual(float(frame.loc[0, "lat"]), 25.0)
        self.assertEqual(float(frame.loc[0, "lon"]), 121.0)

    def test_dataframe_from_text_dispatches_csv(self):
        frame = tgb.dataframe_from_text("lon,lat\n121.0,25.0\n", "sample.csv")

        self.assertEqual(list(frame.columns), ["lon", "lat"])
        self.assertEqual(float(frame.loc[0, "lon"]), 121.0)

    def test_dataframe_from_text_malformed_json_suffix_falls_back_to_csv(self):
        frame = tgb.dataframe_from_text("lon,lat\n121.0,25.0\n", "sample.json")

        self.assertEqual(list(frame.columns), ["lon", "lat"])
        self.assertEqual(float(frame.loc[0, "lat"]), 25.0)

    def test_dataframe_from_text_malformed_jsonl_suffix_falls_back_to_csv(self):
        frame = tgb.dataframe_from_text("lon,lat\n121.0,25.0\n", "sample.jsonl")

        self.assertEqual(list(frame.columns), ["lon", "lat"])
        self.assertEqual(float(frame.loc[0, "lon"]), 121.0)


if __name__ == "__main__":
    unittest.main()
