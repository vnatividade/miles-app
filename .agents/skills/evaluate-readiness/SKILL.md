# Skill — Evaluate Readiness

## Purpose

Evaluate whether a task, ticket or workflow is operationally ready to execute.

This skill prevents:

- unnecessary execution blocking
- false blockers
- hidden dependencies
- operational ambiguity
- premature production requirements

---

# Required Context

Read:

```txt
AGENTS.md
setup/setup-wizard.md
execution/workflow.md
assigned Linear ticket
```

---

# Objective

Determine:

```txt
READY
NOT READY
READY WITH LIMITATIONS
```

based on the actual requirements of the requested task.

---

# Important Principle

Do not require production-grade infrastructure for local or foundational tasks.

Example:

```txt
FastAPI structure creation
!=
Production Datadog setup
```

---

# Required Analysis

## 1. Task Objective

Identify:

- what the task is truly trying to accomplish
- whether execution is local, staging or production-oriented
- whether external integrations are actually required

---

## 2. GO Conditions

Identify what is sufficient to proceed.

GO conditions should be:

- minimal
- objective
- execution-oriented

Example:

```txt
GitHub access
Linear access
setup script functional
```

---

## 3. NO-GO Conditions

Identify what truly blocks execution.

NO-GO conditions should be:

- critical
- unavoidable
- directly related to execution

Avoid inventing blockers.

---

## 4. Optional Dependencies

Identify:

- placeholders
- mocks
- deferred integrations
- future environment dependencies

Example:

```txt
DATABASE_URL placeholder
Datadog not required yet
Railway not required yet
```

---

## 5. Restrictions

Identify:

- what must not be executed
- what must not be configured
- what must not be automated yet

---

# Readiness Levels

## READY

Task can execute safely.

## READY WITH LIMITATIONS

Task can execute with:
- mocks
- placeholders
- local-only assumptions

## NOT READY

Critical blockers exist.

---

# Anti-Patterns

Avoid:

- production paranoia for MVP tasks
- overblocking execution
- requiring unrelated integrations
- assuming all env vars are mandatory
- expanding scope during readiness analysis

---

# Expected Outputs

- readiness verdict
- GO conditions
- NO-GO conditions
- optional dependencies
- restrictions
- execution recommendation
