import os
import pytest
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import app as app_module
from app import app as flask_app


@pytest.fixture(autouse=True)
def isolated_storage(tmp_path, monkeypatch):
    monkeypatch.setattr(app_module, "TASKS_FILE", str(tmp_path / "tasks.json"))


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as c:
        yield c


def test_list_tasks_empty(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert r.get_json() == []


def test_create_task(client):
    r = client.post("/tasks", json={"title": "Buy milk"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["title"] == "Buy milk"
    assert data["done"] is False
    assert "id" in data


def test_create_task_missing_title(client):
    r = client.post("/tasks", json={})
    assert r.status_code == 400


def test_toggle_task(client):
    task = client.post("/tasks", json={"title": "Test"}).get_json()
    r = client.patch(f"/tasks/{task['id']}")
    assert r.status_code == 200
    assert r.get_json()["done"] is True


def test_toggle_task_not_found(client):
    r = client.patch("/tasks/999")
    assert r.status_code == 404


def test_delete_task(client):
    task = client.post("/tasks", json={"title": "Delete me"}).get_json()
    r = client.delete(f"/tasks/{task['id']}")
    assert r.status_code == 200
    tasks = client.get("/tasks").get_json()
    assert all(t["id"] != task["id"] for t in tasks)


def test_delete_task_not_found(client):
    r = client.delete("/tasks/999")
    assert r.status_code == 404
