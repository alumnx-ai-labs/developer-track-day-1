"""Pydantic request/response models. No business logic lives here."""
from datetime import date
from enum import Enum

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    username: str


class UserCreate(BaseModel):
    username: str
    password: str
    full_name: str


class User(BaseModel):
    """Public user representation - never includes the password hash."""
    id: int
    username: str
    full_name: str


class LeaveStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"


class LeaveRequestCreate(BaseModel):
    user_id: int
    start_date: date
    end_date: date
    reason: str


class LeaveRequest(BaseModel):
    id: int
    user_id: int
    start_date: date
    end_date: date
    reason: str
    status: LeaveStatus
