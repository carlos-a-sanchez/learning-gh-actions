## Context

Demo app for a GitHub Actions workshop focused on the Artifacts concept. The app exists to give participants something to build and test in CI — it is not a production system. Simplicity and readability matter more than correctness under load.

## Goals / Non-Goals

**Goals:**
- Single `app.py` file, readable end-to-end in under 5 minutes
- Four REST endpoints covering basic CRUD
- `tasks.json` auto-created at startup if absent
- Pytest suite that generates a JUnit XML report (the artifact)
- Zero runtime deps beyond Flask

**Non-Goals:**
- Authentication or authorization
- Concurrent write safety
- Pagination or filtering
- Persistent IDs across file deletion
- Production-grade error handling

## Decisions

### JSON file over SQLite

SQLite would be more robust, but requires no extra deps either. JSON wins because the storage file is human-readable without any tooling — participants can open it in a text editor and see exactly what the API created. This makes the data layer transparent during the workshop.

Alternative considered: SQLite via built-in `sqlite3` module. Rejected — query strings add cognitive load, and the file isn't inspectable without tooling.

### Auto-increment integer IDs over UUIDs

Integer IDs produce clean URLs (`/tasks/1`) that are easy to type during live demos. UUID URLs (`/tasks/f47ac10b-...`) are harder to use interactively.

### Full file load/save per request

Each request reads the entire JSON file, modifies the in-memory list, and writes it back. No caching, no connection pooling.

Simple and correct for single-user workshop use. Not safe for concurrent writes — acceptable given the context.

### pytest + `--junitxml` for the CI artifact

`pytest --junitxml=report.xml` produces a file in one flag. That file becomes the artifact uploaded in job1 and downloaded in job2. No extra libraries needed.

## Risks / Trade-offs

- **Concurrent write corruption** → Acceptable; workshop runs are single-user
- **File grows unbounded** → Tasks are only deleted explicitly; no auto-cleanup. Fine for demo scale.
- **IDs don't reset on file delete** → IDs are derived from `max(existing ids) + 1`. If the file is deleted and recreated, IDs restart at 1. Acceptable.
