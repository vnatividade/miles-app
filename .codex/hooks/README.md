# Codex Hooks — Disabled Skeleton

## Purpose

Document the intended Codex hook structure for miles-app without enabling runtime automation yet.

This directory exists to prepare future soft-warning hooks around the Agent Activation Pipeline.

Hooks are intentionally disabled in this PR.

---

# Current Status

```txt
Runtime hooks: disabled
Hard blocks: disabled
Soft warnings: not implemented yet
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

Future goal:

- detect missing ticket ID
- detect missing ticket type
- detect approval-gated keywords
- recommend Product Guardian, Risk Reviewer or Billing Strategy when needed

Initial mode:

```txt
soft warning only
```

---

## PreToolUse

Future goal:

- warn before risky commands
- detect potential secrets, deploys, paid ads, real Stripe charging, destructive DB operations or risky provider automation

Initial mode:

```txt
soft warning only
```

Potential later mode:

```txt
selective hard block for secrets, production, payment activation or destructive commands without explicit approval marker
```

---

## Stop

Future goal:

- remind agents to complete handoff
- remind agents to include activation checks performed
- remind agents to recommend next ticket

Initial mode:

```txt
soft warning only
```

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
policy-keywords.yml
README.md
```

Future implementation files may include:

```txt
session_start_reminder.py
user_prompt_activation_check.py
pre_tool_risk_check.py
stop_handoff_check.py
```

Do not add executable hooks without a dedicated implementation ticket.

---

# Non-Goals

This skeleton does not:

- enable hooks
- run scripts
- block commands
- change Codex Cloud behavior
- replace PR review
- replace Linear governance
- replace Product Guardian
- replace human approval

---

# Recommended Next Steps

1. Implement Stop hook as soft warning.
2. Implement UserPromptSubmit hook as soft warning.
3. Evaluate PreToolUse risk-warning hook.
4. Only later evaluate selective hard blocks.
