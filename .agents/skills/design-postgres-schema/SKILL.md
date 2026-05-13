# Skill — Design PostgreSQL Schema

## Purpose

Design PostgreSQL schemas aligned with miles-app operational and product needs.

---

# Required Context

Read:

```txt
AGENTS.md
architecture/data-model.md
architecture/architecture.md
assigned Linear ticket
```

---

# Objective

Create schemas that are:
- explicit
- evolvable
- traceable
- operationally safe

---

# Responsibilities

This skill covers:

- entity modeling
- relationships
- indexes
- constraints
- naming conventions
- migration planning
- raw payload persistence
- historical data preservation

---

# Data Principles

## Preserve Raw Provider Data

Raw payloads must always be persisted.

## Normalize Carefully

Normalize shared concepts without losing provider-specific context.

## Preserve Historical State

Search history is strategic data.

## Explicit Relationships

Relationships should be understandable without hidden assumptions.

---

# Initial Concerns

Focus initially on:

- operational correctness
- traceability
- migration safety
- query clarity

Do not optimize prematurely for extreme scale.

---

# Recommended Standards

## IDs

Use UUIDs where appropriate.

## Timestamps

Every important entity should contain:

```txt
created_at
updated_at
```

## Search Results

Search results should preserve:

- execution source
- provider
- timestamps
- raw payload reference

---

# Anti-Patterns

Avoid:

- catch-all JSON tables
- unclear relationship naming
- duplicated persistence logic
- hidden data coupling

---

# Expected Outputs

- entity diagrams
- PostgreSQL schema proposals
- migration guidance
- index recommendations
- documentation updates
