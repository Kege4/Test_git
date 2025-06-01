# src/converter.py

KM_TO_MILES_RATIO = 0.621371


def km_to_miles(km: float) -> float:
    """
    Convert kilometers to miles. Raises ValueError if input is negative.
    """
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return round(km * KM_TO_MILES_RATIO, 3)


def miles_to_km(miles: float) -> float:
    """
    Convert miles to kilometers. Raises ValueError if input is negative.
    """
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    return round(miles / KM_TO_MILES_RATIO, 3)
