# Task Contract Template

## Objective

Describe exactly what should be delivered.

Example:

```txt
Create the initial FastAPI backend structure for local development.
```

---

# Execution Context

## Environment

```txt
local
staging
production
codex-cloud
```

## Ticket

```txt
PIP-X
```

---

# GO Conditions

Define what is sufficient for execution.

Only include conditions that are truly necessary.

Example:

```txt
- GitHub access
- Linear access
- setup script working
- repository contains AGENTS.md
```

---

# NO-GO Conditions

Define what truly blocks execution.

Only include critical blockers.

Example:

```txt
- cannot create branch
- cannot read repository
- setup script fails completely
```

---

# Optional Dependencies

Define:

- placeholders
- mocks
- deferred integrations
- future setup requirements

Example:

```txt
- DATABASE_URL may remain placeholder
- Datadog not required yet
- Railway not required yet
```

---

# Restrictions

Define what must NOT happen.

Example:

```txt
- do not deploy
- do not configure production secrets
- do not expand MVP scope
- do not implement scraping yet
```

---

# Done Criteria

Define what indicates completion.

Example:

```txt
- FastAPI app starts locally
- /health responds
- Dockerfile exists
- PR created
- handoff documented
```

---

# Risks

List relevant risks.

Example:

```txt
- scope creep
- placeholder assumptions
- missing future integrations
```

---

# Handoff Expectations

Define what the next agent/human must understand.

Example:

```txt
- which files were created
- which integrations remain mocked
- what should happen next
```
