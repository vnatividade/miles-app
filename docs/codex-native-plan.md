# Codex-Native Execution Plan — miles-app

## Purpose

This document defines how miles-app should evolve into a Codex-native agentic repository.

The goal is to make Codex effective at:
- understanding product context
- using Linear as operational source of truth
- executing tickets safely
- creating pull requests with handoff
- preserving continuity across agents

---

# Current Foundation

Already available:

- `AGENTS.md`
- `CLAUDE.md`
- `.cursor/rules/`
- `product/`
- `architecture/`
- `execution/`
- `agents/`
- `.github/pull_request_template.md`
- Linear project: `miles-app`

---

# Target Stack

```txt
AGENTS.md
→ .agents/skills/
→ .codex/config.toml
→ .codex/agents/
→ Linear MCP
→ PR + handoff workflow
```

---

# Phase 1 — Skills Foundation

Create reusable skills that Codex can invoke when working on common workflows.

Initial skills:

- `execute-linear-ticket`
- `prepare-pr-handoff`
- `update-project-docs`

Goal:
- standardize execution behavior
- reduce prompt repetition
- make handoff consistent

---

# Phase 2 — Codex Project Configuration

Create `.codex/config.toml` with safe project-level defaults.

Include:
- AGENTS.md discovery settings
- agent thread limits
- optional MCP placeholders
- no secrets

---

# Phase 3 — Subagents

Create Codex subagents for focused roles:

- `ticket_orchestrator`
- `backend_architect`
- `scraper_engineer`
- `database_designer`
- `product_guardian`

Goal:
- split planning, implementation, review and product scope control

---

# Phase 4 — Linear Operating Loop

Connect Codex to Linear through native integration or MCP.

Expected flow:

```txt
Linear issue
→ Codex task
→ branch
→ implementation
→ PR
→ handoff comment
→ next issue
```

---

# Phase 5 — Quality Gates

Introduce validation rules before PRs are considered ready:

- ticket reference exists
- scope is respected
- tests or validation steps are documented
- docs are updated when needed
- handoff is present
- risks are registered

---

# Phase 6 — Automation Layer

Add hooks/workflows where supported.

Potential automation:

- validate PR template completion
- check Linear ticket reference
- require handoff notes
- suggest next ticket
- update changelog or decision log

---

# Operating Rule

Do not optimize for agent autonomy before operational clarity.

First make the workflow consistent.
Then make it faster.
Then make it more autonomous.
