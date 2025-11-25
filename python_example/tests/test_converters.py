import unittest

from python_example import converters


class TestConverters(unittest.TestCase):
    def test_temperature_roundtrip(self):
        c = 100.0
        f = converters.celsius_to_fahrenheit(c)
        self.assertAlmostEqual(converters.fahrenheit_to_celsius(f), c, places=6)

    def test_distance_roundtrip(self):
        mi = 42.0
        km = converters.miles_to_kilometers(mi)
        self.assertAlmostEqual(converters.kilometers_to_miles(km), mi, places=6)

    def test_weight_roundtrip(self):
        kg = 70.0
        lb = converters.kilograms_to_pounds(kg)
        self.assertAlmostEqual(converters.pounds_to_kilograms(lb), kg, places=6)


if __name__ == "__main__":
    unittest.main()
