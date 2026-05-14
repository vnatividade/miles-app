# Runtime Payload Validation Observation Log — PIP-51

## Summary

PIP-51 prepared the runtime payload validation protocol, but full validation still requires execution inside the actual Codex hook runtime.

This repository-level change does not permanently enable hooks.

```txt
Date: 2026-05-14
Runtime hooks permanently enabled: No
Hard blocks enabled: No
Runtime payload shape fully validated: No
Validation protocol added: Yes
```

---

# What Was Completed

- Added a safe runtime payload validation protocol.
- Defined validation scenarios for Stop, UserPromptSubmit and PreToolUse.
- Defined observation log template.
- Defined compatibility decision categories.
- Kept runtime hooks disabled.

---

# What Was Not Completed

Actual Codex runtime payloads were not observed in this repository-only execution context.

The following still require running inside the target Codex runtime environment:

- observe Stop payload shape
- observe UserPromptSubmit payload shape
- observe PreToolUse payload shape
- compare actual fields against current parser assumptions
- decide whether parser adjustment is needed

---

# Current Parser Assumptions

## Stop

Current extraction candidates:

```txt
message
prompt
response
transcript
text
raw_text
```

## UserPromptSubmit

Current extraction candidates:

```txt
prompt
message
text
input
raw_text
```

## PreToolUse

Current extraction candidates:

```txt
command
tool_input
input
args
message
raw_text
```

---

# Compatibility Status

```txt
Stop: Pending runtime observation
UserPromptSubmit: Pending runtime observation
PreToolUse: Pending runtime observation
```

---

# Sensitive Data Handling

Runtime validation must not collect raw secrets.

Payload inspection should prefer summaries:

- top-level keys
- nested keys
- value types
- redacted string samples when needed

Do not commit raw payloads unless reviewed and sanitized.

---

# Decision

```txt
Proceed to PIP-52 only after runtime payload shape is actually observed.
```

However, if the team wants to keep moving without enabling hooks, the safer path is:

```txt
Keep hooks disabled
→ return to product setup tickets PIP-24 and PIP-27
→ revisit runtime enablement later
```

---

# Recommendation

Do not enable runtime hooks yet.

Recommended next action:

```txt
Run the runtime payload validation protocol in the actual Codex environment.
```

If that is not practical now:

```txt
Park PIP-52 and return to PIP-24 / PIP-27.
```
