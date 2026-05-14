# Manual Test Plan — Codex Soft-Warning Hooks

## Purpose

Validate the existing Codex soft-warning scripts manually/local-only before considering runtime enablement.

This document covers:

- `stop_handoff_check.py`
- `user_prompt_activation_check.py`
- `pre_tool_risk_check.py`

Runtime hooks remain disabled.

---

# Safety Rules

These tests must not:

- enable Codex runtime hooks
- mutate repository files
- access network
- access secrets
- block execution
- change production configuration
- run destructive commands

Expected behavior:

```txt
scripts print advisory warnings
scripts always exit 0
```

For risky PreToolUse scenarios, use **synthetic payloads only**. Do not run real provider, production, billing, credential, destructive data or destructive filesystem commands.

---

# Prerequisites

Run from repository root.

```bash
python3 --version
ls .codex/hooks/stop_handoff_check.py
ls .codex/hooks/user_prompt_activation_check.py
ls .codex/hooks/pre_tool_risk_check.py
```

---

# Test 1 — Stop Hook With Missing Handoff Fields

## Command

```bash
printf '%s' '{"response":"Implemented the task."}' \
  | python3 .codex/hooks/stop_handoff_check.py
```

## Expected Result

The script should:

- print `[Codex soft warning] Handoff reminder`
- list missing fields
- include recommended handoff shape
- exit with code `0`

## Check Exit Code

```bash
echo $?
```

Expected:

```txt
0
```

---

# Test 2 — Stop Hook With Complete Handoff Fields

## Command

```bash
cat <<'JSON' | python3 .codex/hooks/stop_handoff_check.py
{
  "response": "Activation checks performed: roadmap_orchestrator. Files changed: README.md. Tests/checks run: documentation-only. Risks: none. Pending items: none. Suggested next ticket: PIP-99. Human approval required before continuing: No."
}
JSON
```

## Expected Result

The script should:

- print `[Codex soft warning] Handoff reminder`
- indicate required handoff fields appear to be present
- exit with code `0`

---

# Test 3 — UserPromptSubmit Hook With Missing Ticket And Type

## Command

```bash
printf '%s' '{"prompt":"Implement the next thing."}' \
  | python3 .codex/hooks/user_prompt_activation_check.py
```

## Expected Result

The script should warn that:

- no `PIP-X` ticket ID was detected
- no ticket type was detected
- preflight shape should be completed
- exit code is `0`

---

# Test 4 — UserPromptSubmit Hook With Ticket And Backend Type

## Command

```bash
printf '%s' '{"prompt":"Execute PIP-99 as a backend ticket and update the API endpoint."}' \
  | python3 .codex/hooks/user_prompt_activation_check.py
```

## Expected Result

The script should:

- not warn about missing ticket ID
- detect possible ticket type `backend`
- print recommended preflight shape
- exit with code `0`

---

# Test 5 — UserPromptSubmit Hook With Approval-Gated Billing Language

## Command

```bash
printf '%s' '{"prompt":"Execute PIP-99 billing ticket to configure Stripe checkout and subscription payment."}' \
  | python3 .codex/hooks/user_prompt_activation_check.py
```

## Expected Result

The script should:

- detect ticket ID
- detect ticket type `billing`
- detect approval-gated billing/Stripe language
- recommend agents such as:
  - product_guardian
  - billing_strategy_agent
  - risk_reviewer
- remind to confirm human approval requirements
- exit with code `0`

---

# Test 6 — UserPromptSubmit Hook With Provider/Scraper Risk Language

## Command

```bash
printf '%s' '{"prompt":"Execute PIP-99 scraper/provider ticket for real provider scraping with anti-bot concerns."}' \
  | python3 .codex/hooks/user_prompt_activation_check.py
```

## Expected Result

The script should:

- detect ticket ID
- detect scraper/provider language
- detect approval-gated provider/scraping risk
- recommend agents such as:
  - product_guardian
  - risk_reviewer
  - software_architect
- exit with code `0`

---

# Test 7 — Invalid JSON Payload

## Command

```bash
printf '%s' 'not-json prompt with deploy and secrets' \
  | python3 .codex/hooks/user_prompt_activation_check.py
```

## Expected Result

The script should:

- not crash
- treat input as raw text
- detect possible approval-gated language for deploy/secrets
- exit with code `0`

---

# Test 8 — PreToolUse Hook With Safe Test Command

## Command

```bash
printf '%s' '{"command":"pytest"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- print `[Codex soft warning] PreToolUse risk check`
- indicate no high-risk command pattern was detected
- avoid recommending risk agents
- exit with code `0`

---

# Test 9 — PreToolUse Hook With Safe Git Command

## Command

```bash
printf '%s' '{"command":"git status"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- indicate no high-risk command pattern was detected
- exit with code `0`

---

# Test 10 — PreToolUse Hook With Secrets/Credentials Risk

## Synthetic Payload

Do not use a real command that reads environment files or credentials.

Use a synthetic command string that represents this category in a safe way:

```bash
printf '%s' '{"command":"SIMULATED_SECRET_EXPOSURE_COMMAND with API_KEY TOKEN SECRET PASSWORD"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- print `[Codex soft warning] Potential risky command detected`
- classify or approximate the category as `secrets / credentials`
- recommend agents such as:
  - risk_reviewer
  - readiness_validator
- remind that human approval may be required depending on environment and scope
- exit with code `0`

---

# Test 11 — PreToolUse Hook With Production Deploy Risk

## Synthetic Payload

Do not execute any real deployment command.

```bash
printf '%s' '{"command":"SIMULATED_PRODUCTION_DEPLOY_COMMAND deploy production runtime"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `production deploy / runtime mutation`
- recommend agents such as:
  - risk_reviewer
  - readiness_validator
- remind to confirm human approval
- exit with code `0`

---

# Test 12 — PreToolUse Hook With Destructive Database Risk

## Synthetic Payload

Do not execute any real destructive database command.

```bash
printf '%s' '{"command":"SIMULATED_DESTRUCTIVE_DATABASE_COMMAND drop database truncate table"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `destructive database / data operation`
- recommend agents such as:
  - risk_reviewer
  - software_architect
- remind to confirm environment and approval
- exit with code `0`

---

# Test 13 — PreToolUse Hook With Billing/Stripe Risk

## Synthetic Payload

Do not execute real billing provider commands.

```bash
printf '%s' '{"command":"SIMULATED_STRIPE_BILLING_COMMAND stripe checkout subscription payment create"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `billing / Stripe payment operation`
- recommend agents such as:
  - product_guardian
  - billing_strategy_agent
  - risk_reviewer
- remind to confirm test mode, monetization strategy and human approval
- exit with code `0`

---

# Test 14 — PreToolUse Hook With Paid Ads/Budget Risk

## Synthetic Payload

Do not execute paid ads or budget spend commands.

```bash
printf '%s' '{"command":"SIMULATED_PAID_ADS_COMMAND campaign launch budget spend"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `paid ads / budget spend`
- recommend agents such as:
  - product_guardian
  - growth_experiment_agent
  - risk_reviewer
- remind to confirm budget cap and human approval
- exit with code `0`

---

# Test 15 — PreToolUse Hook With Risky Provider Scraping

## Synthetic Payload

Do not execute real provider scraping.

```bash
printf '%s' '{"command":"SIMULATED_PROVIDER_SCRAPING_COMMAND scraper provider live anti-bot captcha"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `risky provider scraping`
- recommend agents such as:
  - product_guardian
  - risk_reviewer
  - software_architect
- remind to confirm provider risk review and scope
- exit with code `0`

---

# Test 16 — PreToolUse Hook With Dangerous Filesystem Operation

## Synthetic Payload

Do not execute destructive filesystem commands.

```bash
printf '%s' '{"command":"SIMULATED_DANGEROUS_FILESYSTEM_COMMAND remove repository metadata recursively"}' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- classify or approximate the category as `dangerous filesystem operation`
- recommend `risk_reviewer`
- remind to confirm intent
- exit with code `0`

---

# Test 17 — PreToolUse Hook With Invalid JSON Payload

## Command

```bash
printf '%s' 'not-json simulated deploy production command' \
  | python3 .codex/hooks/pre_tool_risk_check.py
```

## Expected Result

The script should:

- not crash
- treat input as raw text
- classify or approximate the category as `production deploy / runtime mutation`
- exit with code `0`

---

# Pass Criteria

The manual validation passes if:

- all scripts exit `0`
- missing data produces warnings, not failures
- complete handoff produces lower-noise output
- approval-gated keywords produce agent recommendations
- PreToolUse safe commands do not produce high-risk warnings
- PreToolUse risky synthetic payloads produce the expected risk category or a clearly relevant approximation
- invalid payloads do not crash scripts
- no files are modified
- no network access is required

---

# Fail Criteria

The manual validation fails if:

- any script exits non-zero
- scripts mutate files
- scripts require network access
- scripts expose or ask for secrets
- scripts block execution
- scripts crash on invalid JSON
- PreToolUse safe commands produce noisy risk warnings
- PreToolUse risky synthetic payloads do not produce a relevant risk warning
- warnings are too noisy to be useful

---

# Observation Log Template

Use this after running the tests:

```txt
Date:
Environment:
Python version:
Commit SHA:

Test 1 result:
Test 2 result:
Test 3 result:
Test 4 result:
Test 5 result:
Test 6 result:
Test 7 result:
Test 8 result:
Test 9 result:
Test 10 result:
Test 11 result:
Test 12 result:
Test 13 result:
Test 14 result:
Test 15 result:
Test 16 result:
Test 17 result:

False positives observed:
False negatives observed:
Confusing messages:
Recommended copy changes:
Should we enable runtime hooks now? Yes/No
Reason:
Next recommended ticket:
```

---

# Recommendation After Manual Test

If tests pass, do not enable runtime hooks immediately.

Recommended next step:

```txt
Run manual validation for all Codex soft-warning hooks
```

Runtime enablement should happen only after:

1. manual tests pass
2. false positives are acceptable
3. hook payload shape is validated in the actual Codex environment
4. human approval gates remain preserved
