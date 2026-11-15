
# Milestone 4 — Architecture and Design

## Container Architecture

```mermaid
flowchart LR
    U[Student] --> F[React Frontend]
    F -->|HTTP REST API| B[FastAPI Backend]
    B -->|SQLAlchemy| D[(PostgreSQL)]
```

## Task Creation Sequence

```mermaid
sequenceDiagram
    actor Student
    participant React as React Frontend
    participant API as FastAPI Backend
    participant DB as PostgreSQL

    Student->>React: Enter task details
    React->>API: POST /tasks/
    API->>API: Validate input
    API->>DB: Insert task
    DB-->>API: Saved task
    API-->>React: 201 Created
    React-->>Student: Display new task
```

## Changes Since Milestone 3

- Implemented the React task-management dashboard.
- Added FastAPI task creation and retrieval endpoints.
- Integrated PostgreSQL using SQLAlchemy.
- Connected the frontend and backend.
- Added Docker containers for all three services.
- Deferred AI study-plan generation and authentication to future milestones.
