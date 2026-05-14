# PreToolUse Risk-Warning Hook Evaluation

## Purpose

Evaluate whether a future `PreToolUse` Codex hook should be implemented for miles-app to warn before risky tool/command usage.

This is an evaluation document only.

It does not implement or enable runtime hooks.

---

# Current Status

```txt
Runtime hooks: disabled
PreToolUse hook: not implemented
Hard blocks: disabled
```

Existing soft-warning scripts:

```txt
.codex/hooks/stop_handoff_check.py
.codex/hooks/user_prompt_activation_check.py
```

---

# Recommendation Summary

A future `PreToolUse` hook is useful, but it should start as:

```txt
soft-warning only
```

It should warn before clearly risky commands but should not block normal development work.

Hard blocks should only be considered later for extremely high-risk categories such as:

- likely secret leakage
- production deploy without approval marker
- destructive database command
- real payment activation

---

# Why PreToolUse Is Different

`UserPromptSubmit` warns before the task starts.

`Stop` reminds after the task ends.

`PreToolUse` sits in the danger zone:

```txt
right before a tool or shell command runs
```

That makes it more powerful and more annoying if implemented badly.

A noisy PreToolUse hook will teach agents to ignore warnings.

---

# Risk Categories To Detect

## 1. Secrets / Credentials

Examples:

```bash
cat .env
printenv
cat ~/.ssh/id_rsa
cat ~/.aws/credentials
grep -R "API_KEY" .
```

Suggested warning:

```txt
Potential secret exposure. Confirm this is necessary and do not commit or print secrets.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
selective hard block for obvious private key reads or secret exfiltration patterns
```

---

## 2. Production Deploy / Runtime Mutation

Examples:

```bash
railway up
railway deploy
kubectl apply -f production.yaml
terraform apply
vercel --prod
```

Suggested warning:

```txt
Potential production/runtime change. Confirm human approval before proceeding.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
hard block unless approval marker exists
```

---

## 3. Destructive Database / Data Commands

Examples:

```bash
drop database miles_app;
truncate table alerts;
psql $DATABASE_URL -c "delete from users;"
alembic downgrade base
```

Suggested warning:

```txt
Potential destructive database operation. Confirm environment and approval before proceeding.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
hard block for production-targeted destructive commands
```

---

## 4. Billing / Stripe Real Charging

Examples:

```bash
stripe products create
stripe prices create
stripe trigger checkout.session.completed
```

Risk depends heavily on environment.

Suggested warning:

```txt
Potential billing/payment operation. Confirm test mode and monetization approval.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
hard block only for live mode indicators or live keys
```

---

## 5. Paid Ads / Budget Spend

Examples:

```bash
python scripts/create_meta_campaign.py --budget 100
node scripts/launch-ads.js
```

Suggested warning:

```txt
Potential paid acquisition action. Confirm budget cap and human approval.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
hard block for campaign launch commands without approval marker
```

---

## 6. Risky Provider Scraping

Examples:

```bash
python scripts/run_provider_scraper.py --provider azul --live
python scraper.py --bypass-captcha
```

Suggested warning:

```txt
Potential risky provider automation. Confirm provider risk review and scope.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
keep soft warning unless legal/compliance policy becomes clearer
```

---

## 7. Dangerous File-System Commands

Examples:

```bash
rm -rf /
rm -rf .git
find . -type f -delete
```

Suggested warning:

```txt
Potential destructive filesystem command. Confirm intent.
```

Initial mode:

```txt
soft warning
```

Possible future mode:

```txt
hard block for obvious catastrophic patterns
```

---

# Commands That Should Not Trigger Warnings

Avoid warning on normal development commands:

```bash
pytest
ruff check
mypy
alembic upgrade head
python -m pytest
uv sync
poetry install
git status
git diff
```

Noisy hooks are worse than no hooks.

---

# Proposed Future Hook Behavior

## Input

The script should read hook payload from stdin.

Expected fields may vary, so parsing must be defensive.

Useful values to inspect:

- command/tool name
- command arguments
- working directory
- environment name if available

## Output

The hook should print:

```txt
[Codex soft warning] Potential risky command detected
Category:
Matched terms:
Recommended agents:
Human approval required:
Suggested action:
```

## Exit Code

Initial version must always exit:

```txt
0
```

---

# Recommended Agent Mapping

| Risk Category | Recommended Agents |
|---|---|
| secrets / credentials | risk_reviewer, readiness_validator |
| production deploy | risk_reviewer, readiness_validator |
| destructive database | risk_reviewer, software_architect |
| billing / Stripe | product_guardian, billing_strategy_agent, risk_reviewer |
| paid ads | product_guardian, growth_experiment_agent, risk_reviewer |
| provider scraping | product_guardian, risk_reviewer, software_architect |
| dangerous filesystem | risk_reviewer |

---

# Approval Marker Concept

A future implementation may look for explicit approval markers such as:

```txt
APPROVAL_CONFIRMED
HUMAN_APPROVED
APPROVED_FOR_PRODUCTION
```

But this should not be added casually.

Approval markers can become security theater if agents learn to paste them automatically.

If implemented, the marker must be human-provided in the task context or execution contract.

---

# False Positive Risks

## Production Keyword

The word `production` can appear in harmless docs.

Mitigation:

- warn only when combined with deploy/runtime verbs

## Stripe Keyword

Stripe can appear in planning docs.

Mitigation:

- warn strongly only when combined with create/update/live/payment verbs

## Secret Keyword

Secret can appear in policy docs.

Mitigation:

- warn strongly only for file reads, env dumps or credential paths

## Scraper Keyword

Scraper can appear in normal implementation tickets.

Mitigation:

- warn strongly only when combined with live/provider/bypass/captcha/high-frequency indicators

---

# What Must Not Be Automated

The hook must not:

- approve production deploys
- approve billing activation
- approve paid ads
- approve risky scraping
- mutate commands
- mutate files
- call external services
- read secrets intentionally
- upload logs externally
- decide product strategy

---

# Future Implementation Requirements

A future `pre_tool_risk_check.py` should:

- be dependency-free Python
- parse stdin defensively
- inspect command text only
- never mutate files
- never access network
- always exit 0 initially
- have clear category rules
- keep warnings short
- avoid warning on common safe commands
- include manual test cases

---

# Suggested Future Manual Tests

## Secret Read

```bash
cat .env
```

Expected:

```txt
warn: secrets / credentials
```

## Safe Test Command

```bash
pytest
```

Expected:

```txt
no warning or minimal reminder
```

## Deploy Command

```bash
railway deploy
```

Expected:

```txt
warn: production deploy
```

## Stripe Planning Text

```bash
echo "document Stripe billing strategy"
```

Expected:

```txt
low or no warning
```

## Stripe Live Operation

```bash
stripe products create --name Pro
```

Expected:

```txt
warn: billing / Stripe
```

---

# Implementation Recommendation

Create a future implementation ticket:

```txt
Implement PreToolUse risk-warning hook as soft-warning only
```

But only after one of these is true:

1. Stop/UserPromptSubmit manual tests have been run and logged.
2. Codex payload shape has been validated in the actual environment.
3. The team accepts the false-positive risk.

Do not implement hard blocks yet.

---

# Final Decision

```txt
Proceed later with soft-warning PreToolUse hook.
Do not implement in this ticket.
Do not hard-block yet.
Do not enable runtime hooks yet.
```
