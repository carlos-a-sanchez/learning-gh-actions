## Why

Workshop participants need a concrete app to wire GitHub Actions artifact workflows around. A minimal Flask task manager with JSON file storage serves as the demo target — simple enough to understand in minutes, just complex enough to produce uploadable build artifacts (test reports, packages).

## What Changes

- Add `app.py`: single-file Flask REST API with four endpoints (list, create, toggle, delete tasks)
- Add `tasks.json`: auto-created storage file (not committed)
- Add `requirements.txt`: Flask dependency declaration
- Add `tests/test_app.py`: pytest suite that exercises all endpoints

## Capabilities

### New Capabilities

- `task-api`: CRUD REST API for tasks — create, list, toggle done, delete. Backed by a local `tasks.json` file.
- `task-storage`: JSON file read/write layer — loads on each request, writes atomically per operation.
- `task-tests`: Pytest suite covering all four endpoints, used to generate a test report artifact in CI.

### Modified Capabilities

## Impact

- New files only — no existing code touched
- Runtime dependency: Flask
- Test dependency: pytest
- `tasks.json` should be added to `.gitignore`
