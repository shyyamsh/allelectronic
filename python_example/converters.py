"""Simple unit conversion functions for beginners."""

def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32.0) * 5.0 / 9.0


def miles_to_kilometers(mi: float) -> float:
    """Convert miles to kilometers."""
    return mi * 1.609344


def kilometers_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km / 1.609344


def pounds_to_kilograms(lb: float) -> float:
    """Convert pounds to kilograms."""
    return lb * 0.45359237


def kilograms_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg / 0.45359237
