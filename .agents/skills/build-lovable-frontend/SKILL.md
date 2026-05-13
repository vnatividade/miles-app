# Skill — Build Lovable Frontend

## Purpose

Use Lovable as a frontend and UX acceleration layer for miles-app without moving core product logic into Lovable.

---

# Required Context

Before using Lovable, read:

```txt
AGENTS.md
product/prd.md
product/feedback-loop.md
architecture/architecture.md
execution/workflow.md
assigned Linear ticket
```

---

# Objective

Create or iterate frontend experiences for:

- landing page
- onboarding
- alert creation
- opportunity list
- feedback capture
- dashboard MVP

---

# Role of Lovable

Lovable is responsible for:

- UX velocity
- UI scaffolding
- frontend prototyping
- early product validation
- user-facing flows

---

# What Lovable Must Not Own

Lovable must not own:

- scraping logic
- scheduler logic
- matching engine
- database core model
- notification engine
- observability backend
- business-critical backend rules

---

# Recommended Flow

```txt
Linear ticket
→ product context
→ Lovable prompt
→ frontend iteration
→ GitHub sync or export
→ PR review
→ product validation
```

---

# Required Guardrails

## 1. Backend Is Source of Business Logic

Frontend should call backend APIs instead of reimplementing product rules.

## 2. Keep API Contracts Explicit

Any UI that depends on backend data must reference expected API contracts.

## 3. Feedback Loop First

Prioritize UI that validates product value:

- alert setup
- opportunity usefulness
- alert deactivation reason
- user feedback capture

## 4. No Parallel Data Models

Do not create ungoverned data models inside Lovable.

---

# Initial Lovable Prompts Should Produce

- homepage / landing page
- alert creation flow
- opportunity card UI
- feedback prompt UI
- simple dashboard shell

---

# Acceptance Criteria

A Lovable frontend task is complete when:

- UI matches MVP scope
- core logic remains outside Lovable
- API dependencies are documented
- feedback capture is represented
- PR or export is reviewable
- handoff notes exist

---

# Anti-Patterns

Avoid:

- frontend owning business rules
- unreviewed deploys
- UI scope expansion
- polishing before validation

---

# Expected Outputs

- Lovable prompt
- UI scope definition
- frontend artifact or export
- API dependency notes
- handoff for backend integration
