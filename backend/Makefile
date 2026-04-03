.PHONY: venv install sync dev lint format test migrate migrate-create migrate-down migrate-history

# ─── Ambiente virtual ────────────────────────────────────────────────────────

venv:
	uv venv .venv --python 3.12

# ─── Dependências ─────────────────────────────────────────────────────────────

install:
	uv pip install -r requirements.lock

install-dev:
	uv pip install -r requirements-dev.lock

sync:
	uv pip sync requirements.lock

compile:
	uv pip compile requirements.txt -o requirements.lock

compile-dev:
	uv pip compile requirements-dev.txt -o requirements-dev.lock

# ─── Servidor ─────────────────────────────────────────────────────────────────

dev:
	set PYTHONPATH=. && python src/server.py

# ─── Qualidade de código ──────────────────────────────────────────────────────

lint:
	ruff check src/

format:
	ruff format src/

test:
	pytest

# ─── Migrations (Alembic) ─────────────────────────────────────────────────────

migrate:
	alembic upgrade head

migrate-create:
	alembic revision --autogenerate -m "$(MSG)"

migrate-down:
	alembic downgrade -1

migrate-history:
	alembic history --verbose