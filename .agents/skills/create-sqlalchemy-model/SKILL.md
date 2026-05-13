# Skill — Create SQLAlchemy Model

## Purpose

Create SQLAlchemy models and persistence structures following miles-app data model principles.

---

# Required Context

Before implementation read:

```txt
AGENTS.md
architecture/data-model.md
architecture/architecture.md
execution/done-criteria.md
assigned Linear ticket
```

---

# Objective

Implement persistence models that are:
- explicit
- traceable
- migration-friendly
- aligned with the MVP data model

---

# Recommended Responsibilities

## models.py

Defines SQLAlchemy models.

## schemas.py

Defines Pydantic contracts.

## repository.py

Encapsulates database access.

## migrations/

Tracks schema evolution when migration tooling exists.

---

# Data Principles

## 1. Preserve Raw Data

Raw provider payloads must never be discarded.

## 2. Immutable Search Results

Captured search results should not be mutated after creation.

## 3. Traceability

Every captured result should track:
- provider
- execution id
- captured_at
- source input

## 4. Clear Relationships

Relationships should be explicit and documented.

---

# Anti-Patterns

Avoid:
- generic catch-all tables
- unclear JSON-only models for core entities
- premature analytics schema
- hidden persistence side effects

---

# Expected Outputs

- SQLAlchemy model(s)
- Pydantic schema(s), when needed
- repository layer, when needed
- migration notes
- documentation updates if model changes architecture
