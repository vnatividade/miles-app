# Skill — Setup Datadog Observability

## Purpose

Configure Datadog observability for miles-app.

---

# Required Context

Read:

```txt
AGENTS.md
observability/datadog-strategy.md
architecture/infra.md
assigned Linear ticket
```

---

# Objective

Provide technical and business visibility for:
- infrastructure
- backend
- scrapers
- notifications
- product usage

---

# Responsibilities

This skill covers:

- Datadog setup guidance
- structured logging guidance
- monitor planning
- dashboard planning
- APM integration guidance
- scraper metrics strategy
- business metrics strategy

---

# Initial Instrumentation

## Backend

Track:

- requests
- latency
- errors
- exceptions
- healthcheck

## Scrapers

Track:

- provider
- duration
- failures
- result count
- timeout count

## Scheduler

Track:

- job duration
- execution frequency
- failures

## Business

Track:

- active alerts
- opportunities found
- notifications sent

---

# Logging Standard

Prefer structured logs.

Recommended fields:

```txt
service
provider
execution_id
ticket
environment
severity
```

---

# Initial Dashboards

## Technical Dashboard

- API health
- scraper health
- scheduler status
- database status
- error rate

## Product Dashboard

- active alerts
- searches executed
- opportunities found
- notification volume

---

# Important Rule

Only monitor metrics that help drive action.

Avoid vanity observability.

---

# Expected Outputs

- instrumentation plan
- dashboard proposal
- monitor proposal
- logging standards
- docs updates
