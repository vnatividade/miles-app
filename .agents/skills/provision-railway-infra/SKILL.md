# Skill — Provision Railway Infrastructure

## Purpose

Provision and organize Railway infrastructure safely for miles-app.

---

# Required Context

Read:

```txt
AGENTS.md
architecture/infra.md
execution/workflow.md
assigned Linear ticket
```

---

# Objective

Prepare infrastructure that is:
- operationally safe
- observable
- evolvable
- simple to maintain

---

# Responsibilities

This skill covers:

- environment separation
- service setup
- PostgreSQL provisioning
- variable organization
- healthcheck planning
- logs visibility
- backup awareness
- deployment topology

---

# Recommended Initial Services

```txt
backend-api
postgresql
```

Potential future additions:

```txt
redis
worker
scheduler
proxy-layer
```

---

# Environment Strategy

Recommended:

```txt
production
staging
preview
```

---

# Operational Principles

## Simplicity First

Avoid unnecessary infra complexity.

## Traceability

Infrastructure should be understandable by future agents.

## Safe Evolution

Infra should evolve incrementally.

---

# Monitoring Requirements

Infrastructure should expose:

- logs
- CPU
- memory
- healthchecks
- deployment history

---

# Anti-Patterns

Avoid:

- shared staging/production variables
- undocumented manual setup
- hidden deployment dependencies
- infrastructure drift

---

# Expected Outputs

- infra topology proposal
- environment mapping
- deployment notes
- monitoring notes
- operational documentation
