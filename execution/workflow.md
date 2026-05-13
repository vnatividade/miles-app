# Execution Workflow — miles-app

## Purpose

Define how work must move from product rationale to executable tickets, implementation, review, and handoff.

The goal is to ensure that any AI agent or human contributor can understand:
- what needs to be done
- why it matters
- what has already been completed
- what remains pending
- how to continue the work safely

---

# Source of Truth

## Repository

The repository is the source of truth for:
- product vision
- PRD
- architecture
- technical decisions
- execution rules
- done criteria
- handoff protocol

## Linear

Linear is the source of truth for:
- tickets
- status
- priorities
- milestones
- ownership
- execution visibility
- operational progress

---

# Standard Flow

```txt
Product Context
→ Architecture Context
→ Ticket Creation
→ Ticket Execution
→ Pull Request
→ Review
→ Done
→ Handoff
```

---

# Required Steps Before Execution

Before implementing anything, the agent must:

1. Read relevant product documents.
2. Read relevant architecture documents.
3. Check existing tickets in Linear.
4. Create or select one ticket.
5. Confirm the ticket has clear scope.
6. Confirm acceptance criteria.
7. Create or use an appropriate branch.
8. Execute only the ticket scope.

---

# Required Steps After Execution

After executing a ticket, the agent must:

1. Update the ticket status.
2. Document what changed.
3. Document files changed.
4. Document pending items.
5. Open or update a pull request.
6. Add handoff notes for the next agent.
7. Update repository documentation if a structural decision was made.

---

# Ticket Status Flow

```txt
TODO
→ READY
→ IN_PROGRESS
→ IN_REVIEW
→ DONE
→ HANDOFF_READY
```

---

# Execution Rule

No agent should implement work without a ticket.

If no ticket exists, the agent must create one before starting.

---

# Scope Control

Each ticket should be small enough to be completed independently.

Avoid tickets that mix:
- product decisions
- architecture changes
- implementation
- tests
- deployment

Break them into separate tickets when needed.
