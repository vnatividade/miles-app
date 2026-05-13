# Hook — After Ticket Done

## Purpose

Standardize the actions executed after a ticket is completed.

---

# Required Actions

After completing a ticket:

1. Update ticket status in Linear.
2. Summarize implementation.
3. Document files changed.
4. Document pending items.
5. Document risks or technical debt.
6. Suggest next ticket.
7. Confirm handoff exists.

---

# Documentation Rule

If the ticket changed:
- architecture
- workflows
- contracts
- operational behavior

Then repository documentation must be updated.

---

# Expected Output

```txt
Ticket completed:
- Files changed
- Risks
- Pending items
- Suggested next ticket
- Documentation updated: yes/no
```

---

# Important Rule

The next agent should be able to continue execution without relying on conversational memory.
