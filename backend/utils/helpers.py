# backend/utils/helpers.py

from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# ---------- Password Utilities ----------
def hash_password(password: str) -> str:
    """Generate a secure hash for a password."""
    return generate_password_hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    """Check if the password matches the stored hash."""
    return check_password_hash(password_hash, password)

# ---------- Date Utilities ----------
def str_to_date(date_str: str, fmt="%Y-%m-%d") -> datetime.date:
    """Convert string to datetime.date object."""
    return datetime.strptime(date_str, fmt).date()

def date_to_str(date_obj: datetime.date, fmt="%Y-%m-%d") -> str:
    """Convert datetime.date object to string."""
    return date_obj.strftime(fmt)

# ---------- Data Formatting ----------
def format_forecast_data(forecasts):
    """
    Convert list of Forecast objects to JSON-friendly format.
    Expects a list of SQLAlchemy Forecast objects.
    """
    return [
        {
            "product_name": f.product_name,
            "sales_quantity": f.sales_quantity,
            "forecast_date": date_to_str(f.forecast_date)
        }
        for f in forecasts
    ]
