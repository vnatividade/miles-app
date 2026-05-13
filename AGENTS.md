# AGENTS.md — miles-app

## Purpose

This repository is designed for agentic software execution.

Agents operating in this repository must follow the operational and architectural rules defined in repository documentation.

---

# Read First

Before starting work, agents must read:

```txt
product/
architecture/
execution/
agents/
assigned Linear ticket
```

---

# Operational Model

## Repository

Stores:
- product context
- architecture
- workflows
- execution rules
- standards

## Linear

Stores:
- operational execution
- tickets
- milestones
- status
- priorities

---

# Core Rules

- no execution without ticket
- one ticket scope at a time
- avoid unrelated changes
- preserve MVP discipline
- document important decisions
- preserve traceability

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

Avoid:
- premature abstractions
- speculative architecture
- hidden assumptions
- enterprise overengineering

---

# Important Rule

The repository should remain understandable and operable by future agents without requiring conversational memory.
