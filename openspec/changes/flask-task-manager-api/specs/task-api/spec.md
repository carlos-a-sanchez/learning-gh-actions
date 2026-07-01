## ADDED Requirements

### Requirement: List tasks
The API SHALL return all tasks as a JSON array on `GET /tasks`.

#### Scenario: Empty list
- **WHEN** no tasks exist
- **THEN** the response is `200 OK` with body `[]`

#### Scenario: Tasks exist
- **WHEN** one or more tasks have been created
- **THEN** the response is `200 OK` with a JSON array containing all task objects

### Requirement: Create task
The API SHALL create a new task on `POST /tasks` with a JSON body containing `title`.

#### Scenario: Valid creation
- **WHEN** a POST request is sent with `{"title": "Buy milk"}`
- **THEN** the response is `201 Created` with the new task object including `id`, `title`, and `done: false`

#### Scenario: Missing title
- **WHEN** a POST request is sent without a `title` field
- **THEN** the response is `400 Bad Request`

### Requirement: Toggle task done
The API SHALL toggle the `done` field of a task on `PATCH /tasks/<id>`.

#### Scenario: Toggle incomplete to complete
- **WHEN** a PATCH request is sent for a task with `done: false`
- **THEN** the response is `200 OK` with the task object showing `done: true`

#### Scenario: Toggle complete to incomplete
- **WHEN** a PATCH request is sent for a task with `done: true`
- **THEN** the response is `200 OK` with the task object showing `done: false`

#### Scenario: Task not found
- **WHEN** a PATCH request is sent for a non-existent task id
- **THEN** the response is `404 Not Found`

### Requirement: Delete task
The API SHALL remove a task permanently on `DELETE /tasks/<id>`.

#### Scenario: Successful delete
- **WHEN** a DELETE request is sent for an existing task id
- **THEN** the response is `200 OK` and the task no longer appears in `GET /tasks`

#### Scenario: Task not found
- **WHEN** a DELETE request is sent for a non-existent task id
- **THEN** the response is `404 Not Found`
