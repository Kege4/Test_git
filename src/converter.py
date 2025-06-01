# src/converter.py

def km_to_miles(km):
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km * 0.621371


def miles_to_km(miles):
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    return miles * 1.60934

