# tests/test_planner_api.py

from fastapi.testclient import TestClient
from unittest.mock import patch
from backend.main import app

client = TestClient(app)

@patch("backend.api.routes.PlannerAgent.predict")
def test_api_valid_input(mock_predict):
    mock_predict.return_value = [
        "Add password reset endpoint",
        "Send email with secure token",
        "Create password reset form"
    ]
    response = client.post("/planner/", json={
        "user_story": "As a user, I want to reset my password via email."
    })

    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data
    assert isinstance(data["tasks"], list)
    assert all(isinstance(task, str) for task in data["tasks"])
    assert len(data["tasks"]) > 0

@patch("backend.api.routes.PlannerAgent.predict")
def test_api_empty_input(mock_predict):
    mock_predict.return_value = []
    response = client.post("/planner/", json={"user_story": ""})

    assert response.status_code in [400, 500]

def test_api_missing_user_story():
    response = client.post("/planner/", json={})
    assert response.status_code == 422

def test_api_invalid_user_story_type():
    response = client.post("/planner/", json={"user_story": 123})
    assert response.status_code == 422
