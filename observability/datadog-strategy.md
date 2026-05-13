# Datadog Observability Strategy — miles-app

## Purpose

Define the technical and product observability strategy for miles-app using Datadog as the primary monitoring platform.

The goal is to support both:
- technical reliability
- product/business signal visibility

---

# Recommended Stack

```txt
Railway
→ deploy, infrastructure runtime, basic logs and metrics

FastAPI
→ healthcheck, structured logs, traces, app metrics

Datadog
→ APM, logs, traces, monitors, dashboards, alerts

Linear
→ operational follow-up, incidents, bugs and remediation tickets

Codex / Agents
→ investigation, triage, fixes, PRs and handoff
```

---

# Monitoring Philosophy

Start simple.

Monitor only what helps answer:

```txt
Is the system working?
Are scrapers running?
Are users receiving value?
What broke?
What should be fixed next?
```

Avoid dashboards that look smart but do not drive action.

---

# Technical Signals

## API

Track:

- uptime
- `/health` status
- request latency
- error rate
- 4xx/5xx counts
- exception types

---

## Database

Track:

- connection failures
- query errors
- migration failures
- table growth
- slow queries, when available

---

## Scheduler

Track:

- last scheduler run
- failed executions
- duration per job
- missed executions

---

## Scrapers

Track by provider:

- execution count
- success rate
- failure rate
- timeout count
- duration
- result count
- blocked/captcha signals
- last successful execution

---

## Notifications

Track:

- notifications sent
- delivery failures
- retry count
- provider failures

---

# Product / Business Signals

Track:

- active alerts
- alerts created
- searches executed
- opportunities found
- notifications sent
- opportunities per provider
- routes most monitored
- providers with more failures
- users with recurring active alerts

---

# Initial Monitors

## Critical

- API healthcheck failing
- database connection failure
- scheduler stopped
- scraper provider failing repeatedly
- notification provider failing

## Warning

- high API latency
- unusual drop in scraper results
- high timeout rate
- no opportunities found for too long
- high notification retry count

---

# 24/7 Technical Monitoring Agent

The monitoring agent should not start with production write access.

Initial role:

```txt
Observe
→ detect anomaly
→ collect evidence
→ create Linear issue
→ suggest likely cause
→ suggest next action
```

Future role:

```txt
Observe
→ triage
→ propose fix
→ open PR
→ request review
```

---

# Linear Incident Flow

When a relevant anomaly is detected:

1. Create Linear issue.
2. Add evidence.
3. Add affected provider/service.
4. Add severity.
5. Suggest owner/subagent.
6. Link logs/dashboard when available.

---

# Severity Model

## SEV-1

User-facing outage or complete scraper failure.

## SEV-2

Provider-specific failure, notification failure or degraded reliability.

## SEV-3

Non-critical errors, latency warnings or observability gaps.

---

# MVP Rule

Do not overbuild observability before the system has real traffic.

First implement:

- healthcheck
- structured logs
- scraper execution logs
- basic Datadog integration
- critical monitors
- business counters

Then evolve dashboards and agents based on real incidents.
