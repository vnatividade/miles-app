# Skill — Setup Observability

## Purpose

Design technical and business observability for miles-app.

---

# Required Context

Read:

```txt
AGENTS.md
architecture/architecture.md
architecture/infra.md
product/prd.md
assigned Linear ticket
```

---

# Objective

Create observability that allows the team to understand:

- system health
- scraper health
- operational failures
- product usage
- business outcomes

---

# Observability Layers

## Infrastructure

Track:

- CPU
- memory
- disk
- network
- deployment status

---

## Application

Track:

- API latency
- error rates
- exception types
- database connectivity
- scheduler execution

---

## Scrapers

Track:

- provider success/failure
- execution duration
- captcha/block frequency
- result counts
- timeout frequency

---

## Product / Business

Track:

- active alerts
- searches executed
- opportunities found
- notifications sent
- click/open rates
- most monitored routes
- recurring users

---

# MVP Rule

Initial observability should prioritize:
- operational clarity
- debugging capability
- business signal visibility

Do not overbuild dashboards initially.

---

# Important Principle

If the team cannot understand:
- what failed
- why it failed
- whether users are receiving value

then the observability system is insufficient.

---

# Expected Outputs

- metrics proposal
- logging standards
- monitoring plan
- business KPI mapping
- observability documentation
