# Task Contract — PIP-6 Local Database Follow-up

## Objective

Finalize the local database foundation started for PIP-6 and add the smallest usable API path that exercises repository dependency injection.

---

# Execution Context

## Environment

```txt
local
```

## Ticket

```txt
PIP-6
Cloud task: https://linear.app/pipe-venture-builder/issue/PIP-6/design-initial-postgresql-schema
Branch: feature/pip-6-local-database-follow-up
```

---

# GO Conditions

```txt
- repository context read
- Linear PIP-6 located and referenced
- local branch created
- existing local PIP-6 changes preserved
```

---

# NO-GO Conditions

```txt
- cannot read repository
- cannot create or reference local task contract
- test suite cannot run at all
```

---

# Optional Dependencies

```txt
- DATABASE_URL may remain local-only
- PostgreSQL may be validated through docker-compose when Docker is available
- production database credentials are not required
```

---

# Restrictions

```txt
- do not deploy
- do not configure production database
- do not add observability
- do not implement scraping
- do not expand into multi-database support
- do not introduce heavy architecture patterns
```

---

# Done Criteria

```txt
- Alembic migration path works locally or blocker is documented
- service layer consumes repository abstraction through explicit DI
- basic API contract tests cover the new API path and OpenAPI remains available
- local task contract exists and references cloud PIP-6
- handoff documented in Linear and PR
```

---

# Risks

```txt
- Docker/PostgreSQL may be unavailable in the local environment
- PIP-6 cloud scope is broader than the current minimal local foundation
- adding API surface before full domain model must stay intentionally small
```

---

# Handoff Expectations

```txt
- next agent should know that PIP-6 has a local database foundation only
- next agent should know which local migration command was validated
- next agent should continue with the full MVP data model in a separate focused ticket
```

---

# Completion Notes

## What Was Done

```txt
- created local task contract referencing cloud PIP-6
- kept database foundation local-only
- added service layer for loyalty programs over repository abstraction
- added FastAPI /programs route using explicit dependency injection
- added API/OpenAPI tests and config fallback test
- documented local migration commands in README
```

## Validation

```txt
- python -m ruff check .
- python -m pytest
- DATABASE_URL=sqlite:///./local_migration_test.db python -m alembic upgrade head
- DATABASE_URL=postgresql+psycopg://miles_app:miles_app_local@localhost:55432/miles_app python -m alembic upgrade head
```

## Environment Note

```txt
docker compose up -d postgres was blocked because localhost:5432 is already allocated in this environment.
PostgreSQL migration was validated with a temporary postgres:16-alpine container on localhost:55432.
```

## Suggested Next Ticket

```txt
Implement the full MVP persistence model from architecture/data-model.md in focused slices:
User + Alert first, then SearchExecution/SearchResult/Notification.
```
