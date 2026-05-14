# Codex Hooks — Disabled Skeleton

## Purpose

Document the intended Codex hook structure for miles-app without enabling runtime automation yet.

This directory exists to prepare future soft-warning hooks around the Agent Activation Pipeline.

Hooks remain intentionally disabled unless a future implementation ticket explicitly enables them.

---

# Current Status

```txt
Runtime hooks: disabled
Hard blocks: disabled
Soft warnings: implemented but not enabled for Stop, UserPromptSubmit and PreToolUse reminders
```

No file in this directory should execute automatically until a future implementation ticket explicitly enables it.

---

# References

Read first:

```txt
AGENTS.md
execution/workflow.md
execution/product-agent-pipeline.md
execution/ticket-type-activation-matrix.md
execution/codex-activation-automation-plan.md
```

---

# Intended Hook Events

## SessionStart

Future goal:

- remind agents to read required operating docs
- remind agents to classify ticket type
- remind agents to check activation rules

Initial mode:

```txt
soft reminder only
```

---

## UserPromptSubmit

Current script:

```txt
.codex/hooks/user_prompt_activation_check.py
```

Goal:

- detect missing ticket ID when possible
- detect missing ticket type when possible
- detect approval-gated language
- recommend relevant agents for risky language
- remind agents to classify preflight requirements

Mode:

```txt
soft warning only
```

Runtime status:

```txt
disabled by default
```

The script is safe by design:

- no network access
- no file mutation
- no secrets access
- no hard failure
- exits 0

---

## PreToolUse

Current script:

```txt
.codex/hooks/pre_tool_risk_check.py
```

Goal:

- warn before risky commands
- detect potential secrets, deploys, paid ads, billing operations, destructive database/data operations, risky provider automation and dangerous filesystem operations
- recommend relevant agents for risk review

Mode:

```txt
soft warning only
```

Runtime status:

```txt
disabled by default
```

The script is safe by design:

- no network access
- no command mutation
- no file mutation
- no secrets access
- no hard failure
- exits 0

Potential later mode:

```txt
selective hard block for secrets, production, payment activation or destructive commands without explicit approval marker
```

Do not implement hard blocks until soft-warning behavior has been validated.

---

## Stop

Current script:

```txt
.codex/hooks/stop_handoff_check.py
```

Goal:

- remind agents to complete handoff
- remind agents to include activation checks performed
- remind agents to recommend next ticket

Mode:

```txt
soft warning only
```

Runtime status:

```txt
disabled by default
```

The script is safe by design:

- no network access
- no file mutation
- no secrets access
- no hard failure
- exits 0

---

# Soft-Warning-First Policy

Start with reminders.

Avoid blocking useful execution too early.

Hard blocks should only be considered after observing hook behavior and false positives.

---

# Human Approval Preservation

Hooks must not approve risky work.

The following remain approval-gated:

- production deploy
- production secrets
- real Stripe charging
- billing activation
- paid ads launch
- risky provider scraping
- major product pivot
- autonomous continuation into another ticket

Hooks may warn, remind or block obvious violations in the future.

Hooks must not replace human approval.

---

# Files In This Directory

```txt
hooks.json.disabled
README.md
stop_handoff_check.py
user_prompt_activation_check.py
pre_tool_risk_check.py
```

Future implementation files may include:

```txt
session_start_reminder.py
```

Do not enable executable hooks without a dedicated implementation ticket.

---

# Non-Goals

This skeleton does not:

- enable hooks
- block commands
- change Codex Cloud behavior
- replace PR review
- replace Linear governance
- replace Product Guardian
- replace human approval

---

# Recommended Next Steps

1. Test Stop, UserPromptSubmit and PreToolUse hooks locally/manual-only.
2. Validate actual Codex hook payload shape.
3. Decide whether to enable soft-warning runtime hooks.
4. Only later evaluate selective hard blocks.
