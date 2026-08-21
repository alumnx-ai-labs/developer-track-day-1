# Developer 1: Leave Request API

A small FastAPI service for authenticating users, creating users, and submitting leave requests. The application stores data in memory and is intended for local development and testing.

## Requirements

- Python 3.10 or later
- `pip`

## Setup

From this directory:

```bash
cd developer-1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive documentation is available at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

### `POST /login`

Authenticates a user. The application starts with this demo account:

```json
{
	"username": "jdoe",
	"password": "hunter2"
}
```

Successful response:

```json
{
	"token": "dummy-token-1",
	"username": "jdoe"
}
```

Invalid credentials return `401 Unauthorized`.

### `POST /users`

Creates a user. The username must be a valid email address, the password must contain at least eight characters, and `full_name` must not be blank.

```bash
curl -X POST http://127.0.0.1:8000/users \
	-H 'Content-Type: application/json' \
	-d '{
		"username": "asmith@example.com",
		"password": "correcthorse",
		"full_name": "Al Smith"
	}'
```

Returns `201 Created`. Duplicate usernames return `409 Conflict`.

### `POST /leave-requests`

Creates a pending leave request for an existing user. The end date must be on or after the start date.

```bash
curl -X POST http://127.0.0.1:8000/leave-requests \
	-H 'Content-Type: application/json' \
	-d '{
		"user_id": 1,
		"start_date": "2026-09-01",
		"end_date": "2026-09-05",
		"reason": "Vacation"
	}'
```

Returns `201 Created` with a request status of `pending`. Unknown users return `404 Not Found`; invalid date ranges return `400 Bad Request`.

## Run Tests

```bash
pytest test_leave_requests.py
```

The test suite covers successful and failed login attempts, user creation validation, and leave-request validation.

## Project Structure

| File | Purpose |
| --- | --- |
| `main.py` | FastAPI application and route handlers |
| `models.py` | Pydantic request/response models and leave status enum |
| `validation.py` | Password hashing and input validation helpers |
| `test_leave_requests.py` | API tests using FastAPI's `TestClient` |

`config.py` and `reporting.py` contain legacy code and are not used by the API in `main.py`.

## Development Notes

- Users and leave requests are stored in dictionaries in process memory.
- Restarting the server clears newly created users and requests and restores the demo user.
- Authentication currently returns a dummy token; the token is not used to authorize leave-request operations.
- Passwords are hashed before storage, but the SHA-256 implementation is for this demo only and should be replaced with a password-specific algorithm in production.
