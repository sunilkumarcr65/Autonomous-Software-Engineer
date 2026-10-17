# Autonomous Software Engineer (ASE)

Production-oriented foundation for **Issue → Explore → Plan → Code → Test → Review → PR**.

Provides FastAPI, React/TypeScript, PostgreSQL/Redis infrastructure, task state machine, API, tests, Docker Compose, and clean boundaries for repository intelligence, agent runtime, sandbox execution, memory, Git/rollback, and evaluation.

## Run

```bash
docker compose up --build
```

Frontend: http://localhost:5173  
Backend: http://localhost:8000  
API docs: http://localhost:8000/docs

## Design

The HTTP layer does not contain agent logic. The task service owns task state; future agents, repository analysis, sandbox execution, memory, and evaluation will be plugged in as separate services. This avoids a monolithic LLM prototype and allows the system to scale later.
