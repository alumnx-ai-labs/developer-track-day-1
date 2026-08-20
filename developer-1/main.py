"""Leave Request API. /login is the reference pattern other endpoints should follow."""
from fastapi import FastAPI, HTTPException

from models import LoginRequest, LoginResponse
from validation import hash_password, verify_password

app = FastAPI(title="Leave Request API")

# In-memory stores - reset on restart, demo only.
USERS_DB: dict[int, dict] = {
    1: {
        "id": 1,
        "username": "jdoe",
        "password_hash": hash_password("hunter2"),
        "full_name": "Jane Doe",
    }
}
_next_user_id = 2


def _find_user_by_username(username: str) -> dict | None:
    return next((u for u in USERS_DB.values() if u["username"] == username), None)


@app.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    user = _find_user_by_username(payload.username)
    if user is None or not verify_password(payload.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return LoginResponse(token=f"dummy-token-{user['id']}", username=user["username"])


# TODO: POST /users - create an employee
# TODO: POST /leave-requests - submit a request (validation added here)
# TODO: POST /leave-requests/{id}/approve - approve a request
