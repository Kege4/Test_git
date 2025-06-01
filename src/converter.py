def km_to_miles(km):
    """Convert kilometers to miles."""
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km * 0.621371


def miles_to_km(miles):
    """Convert miles to kilometers."""
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    return miles / 0.621371
