# Runtime Payload Validation — Codex Hooks

## Purpose

Validate the actual payload shape received by Codex hooks in the target runtime environment before enabling hooks permanently.

Manual tests prove the scripts behave with synthetic payloads.

They do not prove Codex runtime payload compatibility.

---

# Current Status

```txt
Runtime hooks enabled permanently: No
Hard blocks enabled: No
Manual synthetic validation: PASS
Runtime payload shape: Not validated yet in target environment
```

---

# Scope

This document defines a safe validation protocol for:

- `Stop`
- `UserPromptSubmit`
- `PreToolUse`

It does not enable hooks permanently.

---

# Safety Rules

Payload validation must not:

- collect secrets
- run production deploys
- run billing commands
- run paid ads commands
- run real provider scraping
- log payloads to external services
- enable hard blocks
- mutate repository files automatically

Use intentionally harmless prompts and commands.

---

# Validation Strategy

Use temporary local/runtime hook configuration only.

The validation script should:

- read stdin
- redact sensitive-looking values
- write or print a sanitized payload-shape summary
- avoid storing raw payloads unless manually reviewed
- always exit `0`

Recommended output should focus on structure, not content:

```txt
Event:
Top-level keys:
Nested keys:
Detected command field candidates:
Detected prompt/text field candidates:
Payload value types:
Parser compatibility:
Sensitive values redacted: Yes/No
```

---

# Temporary Probe Script Recommendation

Create a temporary local-only probe such as:

```txt
.codex/hooks/runtime_payload_probe.py
```

Do not commit raw captured payloads.

If committed later, the probe must:

- redact secrets
- write summaries only
- exit 0
- avoid network
- avoid file mutation unless explicitly requested by the tester

---

# Stop Event Validation

## Harmless Scenario

Ask Codex to produce a short final response for a documentation-only task.

Expected validation:

- identify whether final response text appears in payload
- identify field name candidates such as `response`, `message`, `transcript`, `text` or equivalent
- confirm `stop_handoff_check.py` can extract meaningful text or needs parser adjustment

## Success Criteria

```txt
Stop payload shape documented
stop_handoff_check.py compatibility assessed
no sensitive data captured
```

---

# UserPromptSubmit Event Validation

## Harmless Scenario

Submit a prompt like:

```txt
Execute PIP-99 as a documentation ticket and do not change runtime configuration.
```

Expected validation:

- identify whether user prompt text appears in payload
- identify field name candidates such as `prompt`, `message`, `text`, `input` or equivalent
- confirm `user_prompt_activation_check.py` can extract prompt text or needs parser adjustment

## Success Criteria

```txt
UserPromptSubmit payload shape documented
user_prompt_activation_check.py compatibility assessed
no sensitive data captured
```

---

# PreToolUse Event Validation

## Harmless Scenario

Use a safe command such as:

```txt
python3 --version
```

or:

```txt
git status
```

Expected validation:

- identify where command/tool input appears in payload
- identify command field candidates such as `command`, `tool_input`, `input`, `args` or equivalent
- confirm `pre_tool_risk_check.py` can extract command text or needs parser adjustment

## Success Criteria

```txt
PreToolUse payload shape documented
pre_tool_risk_check.py compatibility assessed
no sensitive data captured
```

---

# Observation Log Template

Use this format after runtime validation:

```txt
Date:
Codex environment:
Runtime hook config type:
Runtime hooks enabled temporarily: Yes/No
Hard blocks enabled: No
Commit SHA:

Stop event observed: Yes/No
Stop top-level keys:
Stop text field candidate:
Stop parser compatible: Yes/No
Stop parser adjustment needed:

UserPromptSubmit event observed: Yes/No
UserPromptSubmit top-level keys:
UserPromptSubmit text field candidate:
UserPromptSubmit parser compatible: Yes/No
UserPromptSubmit parser adjustment needed:

PreToolUse event observed: Yes/No
PreToolUse top-level keys:
PreToolUse command field candidate:
PreToolUse parser compatible: Yes/No
PreToolUse parser adjustment needed:

Sensitive data observed: Yes/No
Sensitive data handling notes:

Recommendation:
Next ticket:
```

---

# Compatibility Decision

## Compatible

Use when all scripts can extract the required text/command from actual payloads without changes.

Next step:

```txt
PIP-52 — Evaluate runtime enablement for Codex soft-warning hooks
```

## Compatible With Adjustments

Use when payloads are understandable but scripts need extraction updates.

Next step:

```txt
Adjust hook payload parsing based on runtime payload shape
```

## Not Compatible

Use when payloads do not expose required fields or runtime validation cannot be performed safely.

Next step:

```txt
Keep hooks manual-only and do not enable runtime hooks
```

---

# Recommendation

Do not enable runtime hooks permanently in PIP-51.

PIP-51 should only validate payload shape and document compatibility.

Runtime enablement belongs to PIP-52 or a follow-up ticket after explicit approval.
