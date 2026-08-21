from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_login_success():
    response = client.post("/login", json={"username": "jdoe", "password": "hunter2"})
    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "jdoe"
    assert body["token"]


def test_login_wrong_password():
    response = client.post("/login", json={"username": "jdoe", "password": "wrong"})
    assert response.status_code == 401


def test_login_unknown_user():
    response = client.post("/login", json={"username": "nobody", "password": "x"})
    assert response.status_code == 401

