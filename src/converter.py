# src/converter.py

KM_TO_MILES_RATIO = 0.621371

def km_to_miles(km):
    """Convert kilometers to miles."""
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km * KM_TO_MILES_RATIO


def miles_to_km(miles):
    """Convert miles to kilometers."""
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    return miles / KM_TO_MILES_RATIO
