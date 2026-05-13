# Execution Map — miles-app

## Purpose

Define the recommended execution timeline for miles-app so agents can identify the next logical ticket after completing work.

This document is not a rigid project plan.

It is an operational navigation map for agents and humans.

---

# Core Rule

After completing a ticket, agents must:

1. update handoff
2. review this execution map
3. identify the next logical ticket
4. explain why that ticket is next
5. propose an execution contract
6. wait for approval before executing the next ticket, unless explicitly authorized

---

# Execution Philosophy

Prioritize:

- dependency order
- MVP velocity
- operational safety
- learning speed
- reduced rework

Avoid:

- parallelizing dependent tickets too early
- implementing scrapers before persistence contracts exist
- deploying before healthcheck and setup are stable
- adding production integrations before local/dev foundation exists

---

# Phase 1 — Agentic Foundation

## Goal

Establish the operating system for agentic execution.

## Tickets

```txt
PIP-12 — Create setup wizard and environment configuration guide
PIP-17 — Standardize MCP operational setup
PIP-14 — Setup Railway staging environment
```

## Notes

These tickets support operational readiness but should not block local backend foundation unless their absence directly affects the task.

---

# Phase 2 — Backend Foundation

## Goal

Create the local/dev backend foundation.

## Tickets

```txt
PIP-5 — Initialize backend project structure
PIP-6 — Design initial PostgreSQL schema
PIP-18 — Define initial backend API contracts for frontend MVP
```

## Recommended Order

```txt
PIP-5
→ PIP-6
→ PIP-18
```

## Rationale

Backend structure comes before persistence and API contracts.

Database schema informs API contracts and frontend integration.

---

# Phase 3 — Persistence and Domain Foundation

## Goal

Implement the first durable domain model and persistence layer.

## Candidate Tickets

```txt
PIP-6 — Design initial PostgreSQL schema
PIP-8 — Implement alert configuration model
```

## Recommended Order

```txt
PIP-6
→ PIP-8
```

## Rationale

Alert configuration depends on clear persistence models and validation rules.

---

# Phase 4 — Scraper Infrastructure

## Goal

Create scraper contracts before provider-specific implementations.

## Tickets

```txt
PIP-7 — Create scraper base contract
```

## Future Tickets

```txt
Implement first provider scraper
Persist raw search results
Normalize search results
```

## Rationale

Provider implementations should not start before contracts, persistence expectations and raw-result preservation rules are clear.

---

# Phase 5 — Matching and Notification Foundation

## Goal

Connect captured opportunities to user alerts and notifications.

## Tickets

```txt
PIP-9 — Implement email notification provider
PIP-16 — Setup notification provider integration
```

## Recommended Order

```txt
PIP-16
→ PIP-9
```

## Rationale

Provider setup and constraints should be defined before implementation.

---

# Phase 6 — Observability and Product Learning

## Goal

Make system health and product value visible.

## Tickets

```txt
PIP-10 — Setup Datadog observability foundation
PIP-15 — Implement Datadog instrumentation baseline
PIP-11 — Design user feedback and product learning loop
```

## Recommended Order

```txt
PIP-10
→ PIP-15
→ PIP-11
```

## Rationale

Strategy comes before instrumentation.

Product learning depends on feedback events and measurement points.

---

# Phase 7 — Frontend Validation

## Goal

Use Lovable/frontend work to validate UX and product value.

## Tickets

```txt
PIP-13 — Define Lovable MCP frontend workflow and guardrails
PIP-18 — Define initial backend API contracts for frontend MVP
```

## Recommended Order

```txt
PIP-13
→ PIP-18
```

## Rationale

Lovable workflow defines frontend boundaries.

Backend API contracts reconcile frontend needs with backend ownership.

---

# Next Ticket Selection Rules

## Rule 1 — Prefer Unblocked Dependencies

Choose tickets that unblock multiple future tickets.

## Rule 2 — Avoid Production Work Too Early

Do not prioritize production deploy, secrets or real external integrations before local/dev foundation is stable.

## Rule 3 — Avoid Provider Work Too Early

Do not implement real scrapers before:

- scraper contract exists
- raw payload strategy exists
- persistence model exists

## Rule 4 — Prefer Foundation Before Surface Area

Backend, persistence and contracts should precede broad UI implementation.

## Rule 5 — Keep Execution Narrow

One ticket at a time unless explicitly authorized.

---

# Default Next Ticket After PIP-5

If PIP-5 is complete and no blockers exist, the recommended next ticket is:

```txt
PIP-6 — Design initial PostgreSQL schema
```

Reason:

```txt
The database foundation is required before alert persistence, scraper results, notification history and feedback storage.
```

---

# Default Next Ticket After PIP-6

If PIP-6 is complete and no blockers exist, the recommended next ticket is:

```txt
PIP-8 — Implement alert configuration model
```

Reason:

```txt
Alert configuration is the first user-facing domain entity and depends on the schema foundation.
```

---

# Important Rule

The roadmap orchestrator should recommend the next ticket, not execute it automatically, unless explicitly authorized by the human operator.
