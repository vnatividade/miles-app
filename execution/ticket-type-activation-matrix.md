# Ticket-Type Activation Matrix — miles-app

## Purpose

Define which agents, skills, preflight checks and postflight checks apply to each ticket type.

This document turns the Product Agent Activation Pipeline into an easier operational checklist for Codex, humans and future agents.

Use this file together with:

```txt
AGENTS.md
execution/workflow.md
execution/product-agent-pipeline.md
execution/execution-map.md
.codex/templates/task-contract.md
```

---

# Core Rule

Every ticket must declare a ticket type before execution.

If the type is unclear, classify it using the closest primary type and add secondary types when needed.

Example:

```txt
Primary type: backend
Secondary types: product, risk/security
```

When multiple types apply, run the stricter gates.

---

# Activation Modes

## Required Preflight

Must run before implementation.

## Approval-Gated

Must stop for explicit human approval before execution.

## Required Postflight

Must run after the work is completed.

## Optional / Conditional

Run only if the ticket context requires it.

---

# Global Checks For Every Ticket

All tickets require:

```txt
read AGENTS.md
read execution/workflow.md
read execution/product-agent-pipeline.md
read execution/execution-map.md
read assigned Linear ticket
```

All tickets must produce:

```txt
Activation checks performed
Files changed
Risks
Pending items
Suggested next ticket
```

All tickets must end with:

```txt
roadmap_orchestrator
→ plan-next-execution
```

---

# Ticket-Type Matrix

| Ticket Type | Required Agents | Required Skills | Preflight | Approval Gate | Postflight |
|---|---|---|---|---|---|
| product | product_guardian, roadmap_orchestrator | product-preflight-review, plan-next-execution | Required | If scope expansion/pivot | Required |
| backend | software_architect, roadmap_orchestrator | apply-engineering-standards, plan-next-execution | Required | If production/secrets involved | Required |
| frontend | product_guardian, software_architect, roadmap_orchestrator | product-preflight-review, apply-engineering-standards, plan-next-execution | Required | If new UX scope or external launch | Required |
| infra | risk_reviewer, readiness_validator, roadmap_orchestrator | run-risk-review, evaluate-readiness, plan-next-execution | Required | Always for production/secrets/deploy | Required |
| observability | readiness_validator, software_architect, roadmap_orchestrator | evaluate-readiness, apply-engineering-standards, plan-next-execution | Required | If production monitors/secrets | Required |
| research | research_orchestrator, product_guardian, roadmap_orchestrator | run-research-orchestration, product-preflight-review, plan-next-execution | Required | If research changes roadmap materially | Required |
| growth | product_guardian, content_strategy_agent or growth_experiment_agent, risk_reviewer, roadmap_orchestrator | product-preflight-review, generate-instagram-content or create-growth-experiment, run-risk-review, plan-next-execution | Required | Always for paid ads/publication automation | Required |
| billing | product_guardian, billing_strategy_agent, risk_reviewer, roadmap_orchestrator | product-preflight-review, define-billing-strategy, run-risk-review, plan-next-execution | Required | Always for real charging/Stripe production | Required |
| scraper/provider | product_guardian, risk_reviewer, software_architect, roadmap_orchestrator | product-preflight-review, run-risk-review, apply-engineering-standards, plan-next-execution | Required | Always for real provider scraping if risk unclear | Required |
| risk/security | risk_reviewer, software_architect, roadmap_orchestrator | run-risk-review, apply-engineering-standards, plan-next-execution | Required | If secrets/production/user data | Required |
| documentation | roadmap_orchestrator, optionally product_guardian/software_architect | plan-next-execution | Conditional | No, unless changing governance materially | Required |
| architecture | software_architect, technical_decision_advisor, roadmap_orchestrator | apply-engineering-standards, evaluate-technical-decision, write-adr, plan-next-execution | Required | If irreversible/major decision | Required |
| knowledge | knowledge_curator, roadmap_orchestrator | update-venture-knowledge-base, plan-next-execution | Conditional | No secrets allowed | Required |

---

# Ticket Type Definitions

## Product

Includes:

- PRD changes
- Working Backwards
- MVP scope decisions
- customer discovery
- product hypothesis changes
- feature rationale

Must answer:

```txt
Does this improve learning about user value?
```

---

## Backend

Includes:

- FastAPI endpoints
- services
- repositories
- models
- tests
- persistence behavior

Must follow:

```txt
architecture/engineering-standards.md
```

Required emphasis:

- layered architecture
- pragmatic DDD
- dependency injection
- OpenAPI quality
- tests following Arrange / Act / Assert

---

## Frontend

Includes:

- Lovable flows
- UX behavior
- screens
- frontend/backend contract consumption

Must not introduce business rules outside backend/product docs.

---

## Infra

Includes:

- Railway
- deployment
- environment variables
- secrets
- CI/CD
- runtime config

Production work is approval-gated.

---

## Observability

Includes:

- Datadog
- logs
- traces
- metrics
- monitors
- dashboards
- alerting

Must connect technical signals to product-learning signals when applicable.

---

## Research

Includes:

- NotebookLM
- Consensus
- Manus
- market scans
- scientific validation
- competitor analysis

Research output must become:

```txt
product implication
architecture implication
validation implication
Linear ticket implication
```

---

## Growth

Includes:

- Instagram content
- SEO
- campaigns
- organic distribution
- paid ads experiments

Paid spend is always approval-gated.

---

## Billing

Includes:

- Stripe
- pricing
- checkout
- subscriptions
- payment links
- webhooks

Technical billing work must not start before monetization strategy exists.

---

## Scraper / Provider

Includes:

- airline or loyalty provider scraping
- provider contracts
- anti-bot strategy
- raw/normalized result handling

Must run product value and risk review.

---

## Risk / Security

Includes:

- user data
- secrets
- legal/compliance concerns
- risky automation
- provider access risk
- agent autonomy risk

Use the strictest gate when uncertain.

---

# Preflight Template

Use this in Codex prompts before implementation:

```txt
Before implementation, classify this ticket:

Primary ticket type:
Secondary ticket types:
Activation triggers:
Required agents:
Required skills:
Approval-gated actions:
Human approval required: Yes/No
Decision: proceed / constrain / split / defer / block

Do not implement until required preflight checks are completed.
```

---

# Postflight Template

Use this after implementation:

```txt
Postflight summary:

Ticket completed:
Files changed:
Activation checks performed:
Tests/checks run:
Risks remaining:
Pending items:
Linear status recommendation:
Recommended next ticket:
Human approval required before continuing: Yes/No
```

---

# Codex Prompt Blocks

## Product Ticket

```txt
Ticket type: product

Required activation:
- product_guardian using product-preflight-review
- roadmap_orchestrator using plan-next-execution after completion

Focus:
- user value
- MVP learning
- assumptions vs evidence
- scope discipline

Do not implement technical changes unless the ticket explicitly requires them.
```

---

## Backend Ticket

```txt
Ticket type: backend

Required activation:
- software_architect using apply-engineering-standards
- product_guardian if user-facing behavior changes
- roadmap_orchestrator after completion

Focus:
- layered architecture
- dependency injection
- SOLID
- OpenAPI quality
- 3A tests

Do not expand product scope.
```

---

## Frontend Ticket

```txt
Ticket type: frontend

Required activation:
- product_guardian using product-preflight-review
- software_architect if API contracts are affected
- roadmap_orchestrator after completion

Focus:
- product behavior alignment
- API contract consistency
- no hidden business rules
- validation-first UX
```

---

## Infra Ticket

```txt
Ticket type: infra

Required activation:
- risk_reviewer using run-risk-review
- readiness_validator using evaluate-readiness
- roadmap_orchestrator after completion

Approval-gated if:
- production deploy
- secrets
- billing
- external provider credentials

Do not configure production secrets without explicit approval.
```

---

## Research Ticket

```txt
Ticket type: research

Required activation:
- research_orchestrator using run-research-orchestration
- product_guardian if outputs can change product scope
- roadmap_orchestrator after completion

Focus:
- evidence quality
- source quality
- product implications
- Linear ticket implications

Do not treat research output as validated demand unless supported by customer behavior.
```

---

## Growth Ticket

```txt
Ticket type: growth

Required activation:
- product_guardian using product-preflight-review
- content_strategy_agent or growth_experiment_agent
- risk_reviewer if public automation or paid spend is involved
- roadmap_orchestrator after completion

Approval-gated if:
- paid ads
- automatic publishing
- budget spend

Agents may draft. Humans approve publication/spend.
```

---

## Billing Ticket

```txt
Ticket type: billing

Required activation:
- product_guardian using product-preflight-review
- billing_strategy_agent using define-billing-strategy
- risk_reviewer using run-risk-review
- roadmap_orchestrator after completion

Approval-gated if:
- real charging
- production Stripe
- subscription activation

Do not implement Stripe Checkout before monetization strategy exists.
```

---

## Scraper / Provider Ticket

```txt
Ticket type: scraper/provider

Required activation:
- product_guardian using product-preflight-review
- risk_reviewer using run-risk-review
- software_architect using apply-engineering-standards
- roadmap_orchestrator after completion

Focus:
- provider contract
- legal/operational risk
- raw result preservation
- normalized result contract
- retries/timeouts

Do not implement broad provider coverage without validation.
```

---

# Next Ticket Recommendation Rule

After every ticket, the roadmap_orchestrator must recommend the next ticket using:

```txt
execution/execution-map.md
execution/product-agent-pipeline.md
current Linear milestone
completed ticket handoff
```

The agent must not start the next ticket unless explicitly authorized.

---

# Human Approval Rule

When in doubt, do not continue silently.

Use:

```txt
Recommend
→ explain
→ wait
```

Not:

```txt
assume
→ execute
→ surprise
```

Surprise is great for birthdays. Péssimo para produção, cartão de crédito e scraping duvidoso.
