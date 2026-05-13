# Workflow — Linear Ticket Execution

## Objective

Standardize how Codex agents should execute Linear tickets.

---

# Workflow

```txt
Read Ticket
→ Read Context
→ Select Skill
→ Create Branch
→ Execute
→ Validate Scope
→ Update Docs
→ Prepare PR
→ Prepare Handoff
→ Suggest Next Ticket
```

---

# Required Context

Before implementation read:

```txt
AGENTS.md
product/
architecture/
execution/
agents/
.assistant/skills/
assigned Linear ticket
```

---

# Required Outputs

Execution must produce:

- implementation
- updated docs if needed
- PR notes
- handoff notes
- next ticket suggestion

---

# Scope Rule

Do not implement unrelated changes.

If scope expands:
- stop
- create or suggest another ticket

---

# Operational Rule

The next agent should be able to continue safely without conversational memory.
