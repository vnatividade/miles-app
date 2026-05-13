# Handoff Protocol — miles-app

## Purpose

Ensure that any agent or contributor can continue work safely after another ticket is completed.

---

# Handoff Requirements

Every completed ticket must include:

## 1. What Was Done

Clear summary of implementation.

---

## 2. Files Changed

List all relevant files.

---

## 3. Decisions Made

Document important implementation decisions.

---

## 4. Pending Items

Document what still needs attention.

---

## 5. Risks

Document technical or operational risks.

---

## 6. Suggested Next Ticket

Recommend logical next execution step.

---

# Important Rule

The next agent should never need to reverse engineer the reasoning behind the implementation.

---

# Example

```txt
Completed:
- implemented alert entity
- created database migration
- added validation rules

Files Changed:
- src/models/alert.py
- src/schemas/alert.py
- migrations/001_alert.sql

Pending:
- notification integration
- alert frequency validation

Suggested Next Ticket:
- implement alert scheduler integration
```
