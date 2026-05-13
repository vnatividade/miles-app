# Skill — Reconcile Frontend Backend Contracts

## Purpose

Keep frontend expectations and backend API contracts aligned.

---

# Required Context

Read:

```txt
frontend/lovable-reference.md
product/prd.md
product/feedback-loop.md
architecture/architecture.md
assigned Linear ticket
```

---

# Objective

Prevent frontend/backend drift.

This skill ensures:
- frontend expectations are documented
- APIs match frontend needs
- Lovable changes remain governed
- hidden product logic does not appear in frontend

---

# Responsibilities

This skill covers:

- reviewing Lovable outputs
- extracting frontend requirements
- mapping API dependencies
- identifying missing backend endpoints
- validating MVP scope alignment
- identifying hidden business logic risks

---

# Validation Questions

For every new frontend flow ask:

## 1. Does the backend support this?

If not:
- create ticket
- document required endpoint

## 2. Is the frontend inventing product logic?

If yes:
- move logic to backend

## 3. Is the feature still MVP-aligned?

If not:
- reduce scope
- defer functionality

## 4. Does this create new data requirements?

If yes:
- involve database_architect

---

# Expected Outputs

- API dependency notes
- backend requirement list
- contract reconciliation notes
- missing endpoint list
- scope warnings
- Linear follow-up tickets
