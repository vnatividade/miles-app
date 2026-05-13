# Task Execution — miles-app

## Purpose

Define how agents should execute tickets.

---

# Standard Execution Flow

```txt
Read Context
→ Select Ticket
→ Understand Scope
→ Plan Changes
→ Execute
→ Validate
→ Document
→ Handoff
```

---

# Before Coding

Agents must answer:

- What is the objective?
- Why does this ticket exist?
- What files are expected to change?
- What are the acceptance criteria?
- What should remain untouched?

---

# During Execution

Agents should:
- keep changes scoped
- preserve readability
- avoid hidden side effects
- prefer explicit code
- document important tradeoffs

---

# After Execution

Agents must:
- update ticket status
- update documentation if necessary
- document pending items
- prepare handoff context

---

# Important Rule

Do not solve future hypothetical problems unless they directly block the current ticket.

---

# Preferred Ticket Size

Tickets should be:
- independently executable
- reviewable
- testable
- understandable in isolation
