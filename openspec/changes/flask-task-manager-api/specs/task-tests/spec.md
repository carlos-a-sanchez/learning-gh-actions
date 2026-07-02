## ADDED Requirements

### Requirement: Test coverage for all endpoints
The test suite SHALL include at least one test per endpoint (GET, POST, PATCH, DELETE).

#### Scenario: All endpoints covered
- **WHEN** pytest is run
- **THEN** tests exist for GET /tasks, POST /tasks, PATCH /tasks/<id>, and DELETE /tasks/<id>

### Requirement: Use Flask test client
Tests SHALL use Flask's built-in test client so no running server is needed.

#### Scenario: Tests run without a server
- **WHEN** pytest is invoked
- **THEN** all tests pass without starting a live HTTP server

### Requirement: Isolated test storage
Tests SHALL use a temporary `tasks.json` file that is created and removed per test, so tests do not share state.

#### Scenario: Test isolation
- **WHEN** two tests run sequentially
- **THEN** tasks created in the first test do not appear in the second test

### Requirement: JUnit XML report generation
Running `pytest --junitxml=report.xml` SHALL produce a valid JUnit XML file consumable as a GitHub Actions artifact.

#### Scenario: Report produced
- **WHEN** pytest is invoked with `--junitxml=report.xml`
- **THEN** `report.xml` exists after the run and contains test result entries
