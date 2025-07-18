# tests/test_planner.py

from agents.planner import PlannerAgent

def test_planner_predict_valid_input():
    agent = PlannerAgent()
    user_story = "As a user, I want to reset my password via a secure link."
    tasks = agent.predict(user_story)

    assert isinstance(tasks, list)
    assert all(isinstance(task, str) for task in tasks)
    assert len(tasks) > 0

def test_planner_predict_empty_input():
    agent = PlannerAgent()
    user_story = ""
    tasks = agent.predict(user_story)

    assert isinstance(tasks, list)
    assert len(tasks) == 0  # or handle however your agent is set up
