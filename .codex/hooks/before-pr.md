# Hook — Before PR

## Purpose

Validate whether a pull request is ready to be opened or marked as ready for review.

---

# Required Checks

Before opening or updating a PR, verify:

- Linear ticket is referenced
- branch name contains ticket identifier
- PR template is completed
- scope matches ticket
- risks are documented
- handoff section is completed
- docs are updated when needed

---

# Failure Conditions

Do not mark PR as ready if:

- no Linear ticket exists
- scope expanded silently
- handoff is empty
- architectural changes were made without docs update
- unrelated files were changed

---

# Expected Output

A short validation summary:

```txt
Before PR validation:
- Ticket: OK / missing
- Scope: OK / expanded
- Docs: OK / required update missing
- Handoff: OK / missing
- Risks: OK / missing
```
