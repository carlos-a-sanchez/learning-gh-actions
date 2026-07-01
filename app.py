import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
    with open(TASKS_FILE) as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


@app.get("/tasks")
def list_tasks():
    return jsonify(load_tasks()), 200


@app.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    if not data.get("title"):
        return jsonify({"error": "title is required"}), 400
    tasks = load_tasks()
    task = {"id": next_id(tasks), "title": data["title"], "done": False}
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201


@app.patch("/tasks/<int:task_id>")
def toggle_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "not found"}), 404
    task["done"] = not task["done"]
    save_tasks(tasks)
    return jsonify(task), 200


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "not found"}), 404
    tasks.remove(task)
    save_tasks(tasks)
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True)
