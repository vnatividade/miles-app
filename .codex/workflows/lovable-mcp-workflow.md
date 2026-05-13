# Workflow — Lovable MCP Frontend Flow

## Objective

Standardize how Lovable should be used through MCP and agent orchestration.

---

# Recommended Architecture

```txt
Lovable
→ frontend UX
→ onboarding
→ dashboard
→ feedback capture

FastAPI Backend
→ business logic
→ scraping
→ scheduler
→ matching engine
→ persistence
```

---

# Workflow

```txt
Linear ticket
→ ticket_orchestrator
→ lovable_frontend_builder
→ Lovable MCP interaction
→ frontend export/sync
→ PR review
→ backend integration
→ product validation
```

---

# Frontend Responsibilities

Lovable should prioritize:

- onboarding UX
- alert creation UX
- opportunity cards
- dashboard shell
- notification preferences
- feedback capture flows

---

# Backend Responsibilities

Backend remains responsible for:

- business rules
- scraping logic
- scheduler
- persistence
- authentication rules
- observability
- notifications

---

# API Rule

Frontend should consume explicit backend APIs.

Avoid hidden frontend-only business behavior.

---

# Feedback Loop Priority

The first Lovable flows should reinforce:

- alert creation
- perceived usefulness
- notification interaction
- deactivation reason capture

---

# Acceptance Criteria

A Lovable workflow is complete when:

- UI supports MVP validation
- API dependencies are documented
- frontend scope is controlled
- backend ownership remains explicit
- PR and handoff exist

---

# Anti-Patterns

Avoid:

- frontend becoming hidden backend
- duplicated business rules
- frontend-only persistence logic
- over-polished UI before validation
