"""Interactive CLI demonstrating the converters module."""
from __future__ import annotations

from python_example import converters


def _read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    MENU = (
        "\nChoose an option:\n"
        "1) Celsius -> Fahrenheit\n"
        "2) Fahrenheit -> Celsius\n"
        "3) Miles -> Kilometers\n"
        "4) Kilometers -> Miles\n"
        "5) Pounds -> Kilograms\n"
        "6) Kilograms -> Pounds\n"
        "0) Exit\n"
    )

    while True:
        print(MENU)
        choice = input("Enter choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice == "1":
            c = _read_float("Celsius: ")
            print(f"{c} °C = {converters.celsius_to_fahrenheit(c):.4f} °F")
        elif choice == "2":
            f = _read_float("Fahrenheit: ")
            print(f"{f} °F = {converters.fahrenheit_to_celsius(f):.4f} °C")
        elif choice == "3":
            mi = _read_float("Miles: ")
            print(f"{mi} mi = {converters.miles_to_kilometers(mi):.4f} km")
        elif choice == "4":
            km = _read_float("Kilometers: ")
            print(f"{km} km = {converters.kilometers_to_miles(km):.4f} mi")
        elif choice == "5":
            lb = _read_float("Pounds: ")
            print(f"{lb} lb = {converters.pounds_to_kilograms(lb):.4f} kg")
        elif choice == "6":
            kg = _read_float("Kilograms: ")
            print(f"{kg} kg = {converters.kilograms_to_pounds(kg):.4f} lb")
        else:
            print("Unknown option — please choose a number from the menu.")


if __name__ == "__main__":
    main()
