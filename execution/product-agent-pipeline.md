# Product Agent Activation Pipeline — miles-app

## Purpose

Define when product, discovery, research, risk, roadmap and execution agents must be activated during the miles-app lifecycle.

This file exists to remove dependence on conversational memory.

Agents should not wait for the human operator to remember which product gate should run.

---

# Core Principle

Every meaningful action must answer:

```txt
Which agent/skill should review this before we execute?
```

The goal is not to create bureaucracy.

The goal is to avoid:

- building without validated rationale
- expanding MVP scope silently
- skipping customer discovery
- launching growth before positioning is clear
- implementing billing before monetization is validated
- starting risky technical work without risk review
- finishing tickets without next-step recommendation

---

# Source Of Truth Boundaries

## GitHub Repository

Stores:

- product rationale
- operating rules
- architecture
- execution workflow
- agent and skill definitions
- reusable templates
- handoff documentation

## Linear

Stores:

- tickets
- status
- milestones
- ownership
- operational sequencing
- execution visibility

## Future Knowledge Base

When available, a knowledge base such as Notion MCP may store:

- interview learnings
- decisions
- incident notes
- prompt learnings
- repeated patterns
- market research summaries

Do not store secrets in the knowledge base.

---

# Activation Modes

## Automatic Recommendation

The agent must recommend the relevant agent/skill and explain why.

It may continue only if the current ticket already authorizes that review.

## Required Preflight

The agent must run the relevant review before implementation.

## Approval-Gated

The agent must stop and ask for human approval before proceeding.

Approval-gated actions include:

- production deploy
- secrets configuration
- paid ads launch
- billing activation
- real user charging
- risky provider scraping
- major scope expansion
- autonomous continuation across tickets

---

# Lifecycle Trigger Matrix

| Event / Situation | Required Agent | Required Skill | Mode | Expected Output |
|---|---|---|---|---|
| New idea appears | product_strategist | create-working-backwards-brief | Required Preflight | product promise, target user, assumptions, risks |
| Idea lacks evidence | customer_discovery_agent | run-customer-discovery | Required Preflight | discovery plan and interview script |
| Feature request appears | product_guardian | product-preflight-review | Required Preflight | approve, constrain, defer, split or reject |
| Scope expansion requested | mvp_scope_reviewer | run-mvp-scope-review | Approval-Gated | build/defer/cut decision |
| Ticket has unclear product value | product_guardian | product-preflight-review | Required Preflight | product rationale and decision |
| New research question appears | research_orchestrator | run-research-orchestration | Automatic Recommendation | research plan and evidence output format |
| Behavioral/scientific hypothesis appears | scientific_validation_agent | run-scientific-validation | Automatic Recommendation | evidence summary and limitations |
| Market/SEO/competitor question appears | market_intelligence_agent | run-market-intelligence-research | Automatic Recommendation | market research brief |
| New frontend/Lovable flow is requested | product_guardian | product-preflight-review | Required Preflight | UX/product alignment decision |
| API contract affects frontend | software_architect | apply-engineering-standards | Required Preflight | contract and architecture validation |
| New backend implementation starts | software_architect | apply-engineering-standards | Required Preflight | engineering standards validation |
| New scraper/provider work starts | risk_reviewer | run-risk-review | Approval-Gated | provider risk review and constraints |
| Notification behavior changes | product_guardian | product-preflight-review | Required Preflight | user value and noise-risk review |
| Observability work starts | readiness_validator | evaluate-readiness | Required Preflight | readiness verdict and scope boundaries |
| Infra/deploy/secrets work starts | risk_reviewer | run-risk-review | Approval-Gated | risk decision and mitigations |
| Billing/Stripe work is proposed | billing_strategy_agent | define-billing-strategy | Approval-Gated | monetization rationale before implementation |
| Organic content/growth work starts | content_strategy_agent | generate-instagram-content | Required Preflight | content strategy and approval workflow |
| Paid ads work starts | growth_experiment_agent | create-growth-experiment | Approval-Gated | experiment plan, budget gate, approval owner |
| Ticket finishes | roadmap_orchestrator | plan-next-execution | Required Postflight | next recommended ticket and rationale |
| Important decision made | technical_decision_advisor | write-adr | Required Postflight | ADR or decision note |
| Learning/incident occurs | knowledge_curator | update-venture-knowledge-base | Automatic Recommendation | learning record or incident note |

---

# Product Preflight Rules

Product preflight must happen before implementation when a ticket changes or creates:

- user-facing behavior
- alert configuration
- opportunity display
- notification behavior
- feedback capture
- onboarding
- frontend flows
- pricing/billing
- acquisition/growth surfaces
- provider coverage

The preflight must answer:

```txt
Does this help validate the core product hypothesis?
```

Core hypothesis:

```txt
Users who already care about mileage redemptions will keep alerts active if miles-app finds opportunities that feel relevant enough to reduce manual search behavior.
```

---

# MVP Scope Rules

MVP Scope Review must run before:

- adding a new feature category
- expanding provider coverage
- adding complex UX flows
- implementing billing
- adding paid growth
- creating dashboards beyond what validation needs
- adding AI assistant behavior

Default decision bias:

```txt
If it does not improve learning about user value, defer it.
```

---

# Customer Discovery Rules

Customer Discovery must run when:

- target persona is unclear
- problem intensity is assumed but not validated
- willingness to pay is discussed
- notification preference is uncertain
- provider/program priority is uncertain
- route/date behavior is assumed

Agents must not treat compliments as validation.

Strong validation requires:

```txt
specific past behavior
+
clear pain
+
concrete alert intent
+
willingness to test or pay
```

---

# Research Activation Rules

Use research agents when the decision depends on external evidence.

## Consensus

Use for:

- behavioral mechanisms
- adoption
- trust
- notification fatigue
- engagement
- decision-making

Do not use for:

- TAM
- CAC
- pricing
- SEO
- competitor positioning

## NotebookLM

Use for:

- source synthesis
- founder/VC methodology synthesis
- report analysis
- structured comparisons

## Manus / Market Intelligence

Use for:

- market scan
- competitor scan
- SEO opportunities
- channel research
- campaign angle research

Research outputs must be converted into product implications, not dumped as raw notes.

---

# Risk Review Rules

Risk Review is mandatory before:

- production deploy
- secret handling
- external provider automation
- real scraping against providers
- paid ads
- billing activation
- autonomous agent continuation beyond one ticket
- anything that could create financial, legal, data, reputation or operational risk

Risk review output must classify:

```txt
Approve
Approve with mitigations
Defer
Block
```

---

# Billing Rules

Stripe or billing implementation must not start until monetization strategy exists.

Before technical Stripe work, agents must define:

- what is being sold
- who pays
- when payment is requested
- what behavior proves willingness to pay
- free vs paid boundary
- test vs production environment
- human approval gate

Default order:

```txt
Customer Discovery
→ MVP Scope Review
→ Monetization Strategy
→ Stripe Checkout MVP in test mode
```

---

# Growth Rules

Organic content can be drafted by agents but should be human-reviewed before publication.

Paid ads must always require human approval before spend.

Paid ads require:

- clear audience
- clear hypothesis
- landing/waitlist path
- budget cap
- conversion event
- approval owner
- performance review plan

---

# Postflight Rules

After every ticket, the executing agent must:

1. summarize what changed
2. list files changed
3. list pending items
4. update or propose Linear status update
5. update PR handoff
6. run roadmap_orchestrator
7. recommend the next logical ticket
8. state whether human approval is required before continuing

Do not automatically start the next ticket unless explicitly authorized.

---

# Output Format For Activation Reviews

Every activation review should use this format:

```txt
Activation Trigger:
Agent:
Skill:
Mode: Automatic Recommendation | Required Preflight | Approval-Gated | Required Postflight
Decision: Approve | Approve with Constraints | Defer | Split | Reject | Block
Reasoning:
Required Inputs:
Expected Outputs:
Risks:
Human Approval Required: Yes/No
Next Action:
```

---

# Example Flows

## New Feature Ticket

```txt
New feature ticket
→ product_guardian
→ product-preflight-review
→ software_architect if implementation follows
→ roadmap_orchestrator after completion
```

## Provider Scraper Ticket

```txt
Provider scraper ticket
→ product_guardian for user value
→ risk_reviewer for provider/legal/operational risk
→ software_architect for provider contract
→ roadmap_orchestrator after completion
```

## Billing Ticket

```txt
Billing idea
→ product_guardian
→ customer_discovery_agent if willingness to pay is unvalidated
→ billing_strategy_agent
→ risk_reviewer
→ only then implementation ticket
```

## Growth Ticket

```txt
Growth idea
→ product_guardian
→ content_strategy_agent or growth_experiment_agent
→ risk_reviewer if paid or automated
→ knowledge_curator after learnings
```

---

# Important Rule

The pipeline recommends and enforces review points.

It does not grant unlimited autonomy.

Default behavior:

```txt
one ticket
one scope
one PR
handoff
recommend next
wait for approval
```
