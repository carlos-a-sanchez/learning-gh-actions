## ADDED Requirements

### Requirement: Auto-create storage file
The system SHALL create `tasks.json` with an empty array if the file does not exist at startup.

#### Scenario: First run
- **WHEN** the app starts and `tasks.json` is absent
- **THEN** `tasks.json` is created containing `[]`

### Requirement: Persist tasks across requests
The system SHALL read from and write to `tasks.json` on every mutating request so that data survives between requests.

#### Scenario: Task persists after creation
- **WHEN** a task is created via `POST /tasks`
- **THEN** `GET /tasks` on a subsequent request returns that task

### Requirement: Auto-increment integer IDs
The system SHALL assign each new task an integer ID equal to the current maximum ID plus one, or 1 if no tasks exist.

#### Scenario: First task
- **WHEN** no tasks exist and a task is created
- **THEN** the task receives `id: 1`

#### Scenario: Subsequent task
- **WHEN** tasks with IDs 1 and 2 exist and a new task is created
- **THEN** the new task receives `id: 3`
