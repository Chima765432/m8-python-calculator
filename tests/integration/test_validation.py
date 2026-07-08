# tests/integration/test_validation.py
# Tests for invalid input handling across the API endpoints.

import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_missing_operand(client):
    response = client.post("/add", json={"a": 10})
    assert response.status_code == 400
    assert "b" in response.json()["error"]

def test_non_numeric_operand(client):
    response = client.post("/multiply", json={"a": "hello", "b": 5})
    assert response.status_code == 400
    assert "a" in response.json()["error"]

def test_empty_body(client):
    response = client.post("/subtract", json={})
    assert response.status_code == 400

def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculator" in response.text
