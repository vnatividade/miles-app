# Branching Strategy — miles-app

## Purpose

Define branch naming and isolation strategy.

---

# Main Rules

## main

Production-ready branch.

Should remain stable.

---

# Ticket Branches

Every ticket should have its own branch.

---

# Naming Convention

```txt
feature/<ticket>-description
fix/<ticket>-description
chore/<ticket>-description
```

Examples:

```txt
feature/MILES-12-alert-engine
fix/MILES-21-timezone-bug
chore/MILES-05-project-setup
```

---

# Scope Isolation

A branch should contain:
- one logical change
- one ticket scope
- one implementation objective

Avoid mixing unrelated work.

---

# Pull Request Rule

PRs should:
- remain reviewable
- explain reasoning
- reference ticket
- explain risks
- explain next steps

---

# Merge Rule

Avoid merging incomplete architectural changes.

Prefer:
- incremental progress
- operational stability
- traceable evolution
