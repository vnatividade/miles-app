# Codex Activation Hooks and Automation Plan — miles-app

## Purpose

Define how Codex hooks and lightweight automation can support the miles-app agent activation system without creating brittle, over-blocking or unsafe automation.

This is a planning document.

Do not implement hooks from this file directly without a follow-up implementation ticket.

---

# Background

The repository now has:

```txt
AGENTS.md
execution/workflow.md
execution/execution-map.md
execution/product-agent-pipeline.md
execution/ticket-type-activation-matrix.md
.codex/config.toml
.agents/skills/
.codex/agents/
```

These files define how agents should operate.

The next maturity step is to decide what should be automated and what should remain judgment-based.

---

# Current Codex Capability Assumptions

Based on current Codex documentation, hooks can run deterministic scripts during the Codex lifecycle.

Useful lifecycle events include:

- `SessionStart`
- `UserPromptSubmit`
- `PreToolUse`
- `PermissionRequest`
- `PostToolUse`
- `Stop`

Hooks can be configured through repository or user-level Codex config, including:

```txt
.codex/hooks.json
.codex/config.toml
```

Hooks are useful for deterministic checks, reminders, logging, validation and soft enforcement.

Hooks should not be treated as a replacement for product judgment.

---

# Automation Principle

Automate checklists.

Do not automate judgment.

Good automation:

- detects missing ticket reference
- checks required files exist
- warns if activation matrix is not mentioned
- checks PR/handoff structure
- reminds agent to run Product Guardian
- blocks obvious unsafe actions when configured locally

Bad automation:

- decides product strategy
- approves billing
- launches ads
- bypasses human approval
- blocks all work because one optional field is missing
- pretends to understand legal/compliance risk fully

---

# Safe Automation Boundaries

## Safe To Automate Now

These can be automated with low risk:

- verify `AGENTS.md` exists
- verify `execution/product-agent-pipeline.md` exists
- verify `execution/ticket-type-activation-matrix.md` exists
- remind agent to classify ticket type
- check if a Linear ticket ID appears in prompt/branch/PR body
- check if PR body contains required sections
- warn if activation checks are missing from PR body
- warn if postflight summary is missing
- warn if suggested next ticket is missing
- detect obvious secret-like strings in prompts or changed files
- detect production-sensitive keywords and require approval reminder

## Safe With Caution

These should start as soft warnings:

- detecting billing/Stripe work without monetization strategy mention
- detecting paid ads language without approval gate mention
- detecting provider/scraper implementation without risk review mention
- detecting frontend changes without product preflight mention
- detecting backend endpoint changes without OpenAPI/tests mention

## Not Safe To Fully Automate Yet

Do not fully automate or hard-block initially:

- product approval
- MVP scope decisions
- customer discovery interpretation
- pricing decisions
- paid ads launch decisions
- provider legal/compliance decisions
- production deployment approvals
- Stripe production enablement
- next-ticket execution

---

# Recommended Hook Strategy

## Phase 1 — Documentation-Based Soft Enforcement

Goal:

```txt
Make agents see the correct checklist before and after work.
```

Recommended mechanisms:

- keep `AGENTS.md` and `execution/workflow.md` as primary enforcement
- use `execution/ticket-type-activation-matrix.md` in prompts
- update PR template to include activation checks
- avoid actual blocking hooks initially

Recommended follow-up ticket:

```txt
Add activation checks to PR template
```

---

## Phase 2 — Local Soft-Warning Hooks

Goal:

```txt
Warn when obvious activation rules are missing.
```

Potential files:

```txt
.codex/hooks.json
.codex/hooks/user_prompt_activation_check.py
.codex/hooks/stop_handoff_check.py
.codex/hooks/pre_tool_risk_check.py
```

Recommended events:

### UserPromptSubmit

Use to detect whether the prompt mentions:

- ticket ID
- ticket type
- activation checks
- approval-gated actions

Behavior:

```txt
soft warning only
```

### Stop

Use to remind the agent to include:

- files changed
- activation checks performed
- risks
- pending items
- suggested next ticket

Behavior:

```txt
soft warning only
```

### PreToolUse

Use only for high-risk command warnings.

Examples:

- deployment command
- secret/config mutation
- destructive command
- production environment command

Behavior:

```txt
warn or request approval, not broad blocking
```

---

## Phase 3 — PR/Handoff Validation

Goal:

```txt
Make PRs consistently include activation and handoff metadata.
```

Recommended mechanisms:

- GitHub PR template
- optional GitHub Action / check script later
- Codex stop hook reminder

Validation targets:

- Linear ticket reference
- included/excluded scope
- activation checks performed
- risks
- handoff
- suggested next ticket

Recommended follow-up ticket:

```txt
Update PR template with activation check section
```

---

## Phase 4 — Selective Hard Blocks

Only after soft warnings prove useful.

Possible hard blocks:

- detected secret committed to repo
- production deploy command without explicit approval marker
- paid ads launch command without explicit approval marker
- Stripe live key or live payment activation without approval marker
- destructive database command without approval marker

Do not hard-block normal development work.

---

# Proposed Hook Points

| Hook Event | Purpose | Initial Mode | Hard Block Later? |
|---|---|---|---|
| `SessionStart` | summarize required docs and activation matrix | soft reminder | no |
| `UserPromptSubmit` | classify prompt risk and missing ticket/type | soft warning | maybe for secrets |
| `PreToolUse` | detect risky commands before execution | soft warning | yes for secrets/prod/destructive |
| `PermissionRequest` | add context to approval requests | soft reminder | no |
| `PostToolUse` | inspect command output for failed tests/checks | soft warning | no |
| `Stop` | enforce handoff reminder | soft warning | maybe for missing PR handoff |

---

# Suggested Hook Behaviors

## SessionStart Hook

Print/remind:

```txt
Read AGENTS.md, execution/workflow.md, product-agent-pipeline.md and ticket-type-activation-matrix.md before execution.
```

Do not block.

---

## UserPromptSubmit Hook

Detect:

- missing ticket ID
- missing ticket type
- approval-gated keywords
- risky terms like `production`, `secret`, `Stripe live`, `paid ads`, `deploy`, `scraper provider`

Output:

```txt
Potential activation required: product_guardian / risk_reviewer / billing_strategy_agent
```

Do not block initially.

---

## PreToolUse Hook

Detect risky shell/tool commands:

- deploy commands
- commands touching `.env`, secrets or credentials
- destructive database commands
- commands targeting production
- payment activation commands

Initial behavior:

```txt
warning + approval reminder
```

Future behavior:

```txt
hard block only for secrets/prod/destructive commands without approval marker
```

---

## Stop Hook

At the end of a turn, remind required handoff:

```txt
Activation checks performed:
Files changed:
Tests/checks run:
Risks:
Pending items:
Suggested next ticket:
Human approval required before continuing:
```

Do not block initially.

---

# Recommended Files For Future Implementation

```txt
.codex/hooks.json
.codex/hooks/README.md
.codex/hooks/user_prompt_activation_check.py
.codex/hooks/pre_tool_risk_check.py
.codex/hooks/stop_handoff_check.py
.codex/hooks/policy_keywords.yml
```

---

# Recommended `hooks.json` Shape For Later

This is illustrative only.

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_activation_check.py\"",
            "statusMessage": "Checking activation requirements"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_risk_check.py\"",
            "statusMessage": "Checking risky command"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_handoff_check.py\"",
            "statusMessage": "Checking handoff completeness"
          }
        ]
      }
    ]
  }
}
```

---

# Required Config Change For Later

If hooks are implemented, Codex hook support should be enabled in the active Codex configuration.

Illustrative config:

```toml
[features]
codex_hooks = true
```

This should be validated in the actual Codex Cloud/local environment before relying on it.

---

# Automation Failure Strategy

Start with soft warnings.

Hard blocks should be rare.

## Soft Warning

Use when:

- missing activation metadata
- missing suggested next ticket
- possible scope issue
- possible missing Product Guardian review

## Hard Block

Use only when:

- likely secret leakage
- destructive command
- production deploy without approval marker
- real payment activation without approval marker
- paid ad launch without approval marker

---

# Human Approval Preservation

Hooks must not replace human approval.

Approval-gated actions remain approval-gated:

- production deploy
- production secrets
- real Stripe charging
- paid ads
- risky provider scraping
- major pivot
- autonomous next-ticket execution

The hook may remind, warn or block obvious violations.

The hook must not approve.

---

# Future Implementation Roadmap

## Ticket A — Update PR template with activation checks

Goal:

Add required PR sections:

- activation checks performed
- ticket type
- product/risk/architecture preflight status
- human approval required

Risk: low.

---

## Ticket B — Add Codex hooks documentation and disabled skeleton

Goal:

Add `.codex/hooks/README.md`, example `hooks.json.disabled` and policy docs without enabling runtime hooks yet.

Risk: low.

---

## Ticket C — Implement Stop hook for handoff reminders

Goal:

Warn when handoff sections are missing.

Risk: low.

Mode:

```txt
soft warning only
```

---

## Ticket D — Implement UserPromptSubmit hook for activation reminders

Goal:

Warn when ticket type, ticket ID or activation checks are missing.

Risk: medium.

Mode:

```txt
soft warning only
```

---

## Ticket E — Implement PreToolUse risk warning hook

Goal:

Warn before risky commands.

Risk: medium.

Mode:

```txt
soft warning first
```

---

## Ticket F — Evaluate selective hard blocks

Goal:

After observing hook behavior, decide whether to hard-block secrets, production deploy, destructive DB and payment activation commands without approval marker.

Risk: medium/high.

Requires human approval.

---

# Non-Goals

This plan does not aim to:

- create a full orchestration engine
- replace Linear
- replace PR review
- replace Product Guardian judgment
- automatically approve risky work
- implement production deployment controls
- implement billing or ads automation
- create custom external services

---

# Recommendation

Do not implement hard-block hooks yet.

Recommended next step:

```txt
Update PR template with activation checks
```

Then:

```txt
Add disabled Codex hooks skeleton
→ enable Stop hook as soft warning
→ enable UserPromptSubmit hook as soft warning
→ evaluate PreToolUse risk warnings
→ only later evaluate selective hard blocks
```

This keeps the system useful without making it annoying.

The goal is guardrails, not a bureaucracy goblin sitting on every commit.
