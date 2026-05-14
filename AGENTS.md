# AGENTS.md — miles-app

## Purpose

This repository is designed for agentic software execution.

Agents operating in this repository must follow the operational, product, architectural and activation rules defined in repository documentation.

---

# Read First

Before starting work, agents must read:

```txt
product/
architecture/
execution/
.agents/skills/
.codex/agents/
assigned Linear ticket
```

Minimum required files:

```txt
execution/workflow.md
execution/execution-map.md
execution/product-agent-pipeline.md
architecture/engineering-standards.md
```

---

# Operational Model

## Repository

Stores:

- product context
- architecture
- workflows
- execution rules
- agent activation rules
- standards
- handoff expectations

## Linear

Stores:

- operational execution
- tickets
- milestones
- status
- priorities
- ownership

---

# Core Rules

- no execution without ticket
- one ticket scope at a time
- avoid unrelated changes
- preserve MVP discipline
- document important decisions
- preserve traceability
- check required agent activations before execution
- do not bypass approval-gated actions

---

# Agent Activation Requirement

Before executing a ticket, agents must check:

```txt
execution/product-agent-pipeline.md
```

The agent must identify:

- activation trigger
- required agent
- required skill
- activation mode
- expected output
- whether human approval is required

If a required activation applies, the agent must run or document the review before implementation.

---

# Mandatory Product Gate

For any ticket that affects user-facing behavior, product scope, frontend flow, notifications, provider coverage, billing, pricing, growth or acquisition, agents must invoke:

```txt
product_guardian
→ product-preflight-review
```

Default decision bias:

```txt
If the work does not improve learning about user value, defer it.
```

---

# Approval-Gated Actions

Agents must stop and request human approval before:

- production deploy
- configuring production secrets
- charging real users
- enabling Stripe/billing in production
- launching paid ads
- expanding provider scraping into risky/unclear territory
- making major product pivots
- continuing autonomously into a new ticket

---

# Branching

Use:

```txt
feature/<ticket>-description
fix/<ticket>-description
chore/<ticket>-description
```

---

# Pull Requests

Every PR should contain:

- ticket reference
- context
- included/excluded scope
- activation checks performed
- risks
- handoff
- suggested next ticket

---

# Product Principles

Prefer:

- operational simplicity
- fast learning
- modularity
- explicit code
- evolvable systems
- validated user value

Avoid:

- premature abstractions
- speculative architecture
- hidden assumptions
- enterprise overengineering
- feature work without product rationale
- billing or growth before validation

---

# Postflight Requirement

After completing a ticket, agents must:

1. document changed files
2. document pending items
3. update or propose Linear status update
4. add PR handoff
5. run or invoke roadmap_orchestrator
6. recommend the next logical ticket
7. wait for approval before starting the next ticket

---

# Important Rule

The repository should remain understandable and operable by future agents without requiring conversational memory.
