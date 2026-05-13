# Agent Operating Model — miles-app

## Purpose

Define how AI agents should behave while operating on the repository.

---

# Core Principle

Agents are not autonomous product owners.

Agents are execution systems operating within:
- product constraints
- architecture constraints
- ticket scope
- MVP discipline

---

# Agent Responsibilities

Agents should:
- understand context before executing
- follow repository rules
- work ticket-by-ticket
- preserve operational clarity
- document decisions
- prepare safe handoffs

---

# Agent Restrictions

Agents should NOT:
- expand scope without reason
- redesign architecture without justification
- introduce unnecessary complexity
- modify unrelated systems
- create hidden assumptions

---

# Required Reading Order

Before starting work:

```txt
product/
→ architecture/
→ execution/
→ agents/
→ assigned ticket
```

---

# Operational Rule

If context is unclear:
- stop execution
- document uncertainty
- request clarification

Do not invent business rules.

---

# Documentation Rule

Important implementation decisions must be documented.

---

# MVP Rule

Prefer:
- operational simplicity
- fast learning
- safe iteration

Avoid:
- premature optimization
- enterprise overengineering
- unnecessary abstraction
