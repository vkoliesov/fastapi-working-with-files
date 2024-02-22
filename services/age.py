from datetime import datetime, timedelta

from constants import YEAR_DAYS


def get_current_date():
    """Get current date method."""
    return datetime.now().date()


def calculate_age(birth_date):
    """Calculate age method."""
    current_date = get_current_date()

    age_delta = current_date - birth_date
    return age_delta // 365


def calculate_dates_by_age(age):
    """Calculate date by age method."""
    current_date = get_current_date()
    birth_date_from = current_date - timedelta(age * YEAR_DAYS + 6) # 6 days for leap years

    birth_date_to = birth_date_from + timedelta(years=1) - timedelta(days=1)
    return birth_date_from, birth_date_to
