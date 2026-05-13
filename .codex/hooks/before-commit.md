# Hook — Before Commit

## Purpose

Prevent low-quality or unrelated commits.

---

# Required Checks

Before committing:

- confirm current ticket
- confirm branch naming
- confirm only related files changed
- confirm no secrets are included
- confirm docs updated when needed

---

# Scope Rule

A commit should represent:
- one logical change
- one ticket scope

Avoid mixing unrelated work.

---

# Secret Rule

Never commit:

- API keys
- tokens
- local MCP config
- real .env files
- credentials

---

# Expected Output

```txt
Before commit validation:
- Ticket: OK / missing
- Branch: OK / invalid
- Scope: OK / unrelated files detected
- Secrets: OK / possible leak detected
- Docs: OK / missing updates
```
