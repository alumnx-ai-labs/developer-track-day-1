"""Shared validation utilities. Every endpoint should reuse these instead of inlining checks."""
import hashlib
from datetime import date


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, password_hash: str) -> bool:
    return hash_password(password) == password_hash


def validate_date_range(start_date: date, end_date: date) -> None:
    """Raise ValueError if the range is missing either bound or end precedes start."""
    if start_date is None or end_date is None:
        raise ValueError("start_date and end_date are required")
    if end_date < start_date:
        raise ValueError("end_date must not be before start_date")
