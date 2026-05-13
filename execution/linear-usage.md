# Linear Usage — miles-app

## Purpose

Define how Linear should be used operationally.

---

# Role of Linear

Linear is the operational execution layer.

Linear is responsible for:
- tickets
- status
- priorities
- milestones
- execution visibility
- operational handoff

---

# Repository vs Linear

## Repository

Stores:
- product knowledge
- architecture
- standards
- workflows
- strategic context

## Linear

Stores:
- operational execution
- ticket lifecycle
- active work
- priorities
- blockers

---

# Required Ticket Structure

Every ticket should contain:

- context
- goal
- scope
- acceptance criteria
- technical notes
- risks
- handoff expectations

---

# Branch Naming

Recommended:

```txt
feature/<ticket>-description
fix/<ticket>-description
chore/<ticket>-description
```

Example:

```txt
feature/MILES-12-alert-engine
```

---

# Pull Request Rule

Every PR should reference:
- Linear ticket
- scope
- relevant decisions
- risks
- next steps

---

# Operational Rule

No implementation without:
- existing ticket
- clear acceptance criteria
- defined scope
