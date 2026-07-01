## 1. Project Files

- [x] 1.1 Create `requirements.txt` with Flask as the only dependency
- [x] 1.2 Add `tasks.json` to `.gitignore`

## 2. Storage Layer

- [x] 2.1 Implement `load_tasks()` — reads `tasks.json`, returns list; creates file with `[]` if absent
- [x] 2.2 Implement `save_tasks(tasks)` — writes list to `tasks.json`
- [x] 2.3 Implement `next_id(tasks)` — returns `max(t["id"] for t in tasks) + 1` or `1` if empty

## 3. API Endpoints

- [x] 3.1 `GET /tasks` — return `load_tasks()` as JSON, status 200
- [x] 3.2 `POST /tasks` — validate `title` present, create task with `done: false`, save, return 201
- [x] 3.3 `PATCH /tasks/<id>` — find task by id, toggle `done`, save, return 200; 404 if not found
- [x] 3.4 `DELETE /tasks/<id>` — remove task by id, save, return 200; 404 if not found

## 4. Tests

- [x] 4.1 Create `tests/test_app.py` with pytest fixture using Flask test client and temp `tasks.json`
- [x] 4.2 Test `GET /tasks` returns empty list on fresh storage
- [x] 4.3 Test `POST /tasks` creates task with correct fields and returns 201
- [x] 4.4 Test `POST /tasks` without title returns 400
- [x] 4.5 Test `PATCH /tasks/<id>` toggles done from false to true
- [x] 4.6 Test `PATCH /tasks/<id>` with unknown id returns 404
- [x] 4.7 Test `DELETE /tasks/<id>` removes task and returns 200
- [x] 4.8 Test `DELETE /tasks/<id>` with unknown id returns 404
