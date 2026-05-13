# Skill — Create FastAPI Module

## Purpose

Create new FastAPI modules following miles-app architectural standards.

---

# Required Context

Before implementation read:

```txt
AGENTS.md
architecture/architecture.md
agents/task-execution.md
assigned Linear ticket
```

---

# Objective

Create modular FastAPI functionality while preserving:
- readability
- MVP simplicity
- explicit flows
- evolvability

---

# Recommended Structure

```txt
src/
└── <module>/
    ├── routes.py
    ├── schemas.py
    ├── service.py
    ├── repository.py
    └── models.py
```

---

# Responsibilities

## routes.py

FastAPI endpoints only.

## schemas.py

Pydantic request/response models.

## service.py

Business orchestration.

## repository.py

Persistence access layer.

## models.py

ORM or domain models.

---

# Important Rules

## 1. Explicit APIs

Prefer explicit request and response contracts.

## 2. Avoid Hidden Side Effects

Do not hide important logic inside decorators or magic abstractions.

## 3. Keep Modules Focused

One module should solve one logical domain concern.

## 4. Preserve Traceability

Important operations should be observable and understandable.

---

# Anti-Patterns

Avoid:
- giant service files
- mixed concerns
- tightly coupled modules
- premature generic abstractions

---

# Expected Outputs

- FastAPI routes
- schemas
- services
- repositories
- models
- updated docs if architectural behavior changes
