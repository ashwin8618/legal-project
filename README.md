# Legal application

Modular monolith with a React frontend and a FastAPI backend. The first slice is a hello-world greeting stored in PostgreSQL.

## Layout

```text
frontend/     React, Vite, Tailwind CSS, shadcn/ui, Vitest
backend/      FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, pytest
docker-compose.yml
```

Feature code lives in modules. The hello module is `frontend/src/modules/hello` and `backend/app/modules/hello`. Shared backend infrastructure is in `backend/app/core`. New features should follow that split and be registered in `backend/app/api.py`.

## Prerequisites

- Node.js 22.12+ or 24+
- Python 3.11+
- Docker with Compose, for the full stack

## Run with Docker

```bash
cp .env.example .env
docker compose up --build
```

- App: http://localhost:5173
- API: http://localhost:8000/api/v1/hello
- API docs: http://localhost:8000/docs

PostgreSQL is `pgvector/pgvector:pg17`. The first migration enables the `vector` extension and creates `hello_messages`.

## Run locally

Start PostgreSQL with `docker compose up db`, then:

```bash
cp .env.example .env

cd backend
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
alembic upgrade head
uvicorn app.main:app --reload

cd frontend
npm install
npm run dev
```

The Vite dev server proxies `/api` to `http://localhost:8000`.

## Tests

```bash
cd backend && .venv/bin/pytest
cd frontend && npm test
```

Backend HTTP tests use SQLite, so they do not need PostgreSQL. pgvector is covered by the migration and by a type import test.
