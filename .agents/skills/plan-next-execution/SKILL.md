# Skill — Plan Next Execution

## Purpose

Determine the next logical ticket after completing a task.

This skill exists to:

- preserve execution order
- avoid dependency violations
- preserve MVP velocity
- reduce operational ambiguity
- prevent autonomous scope explosion

---

# Required Context

Read:

```txt
execution/execution-map.md
AGENTS.md
assigned Linear ticket
related milestones
handoff notes
```

---

# Objective

After a ticket is completed:

1. identify what changed
2. identify what was unblocked
3. identify the next logical ticket
4. explain why
5. define execution constraints
6. wait for approval unless explicitly authorized

---

# Decision Criteria

Prioritize:

- dependency order
- foundation before expansion
- MVP learning velocity
- low operational risk
- tickets that unblock multiple future tickets

Avoid:

- production hardening too early
- real provider implementation too early
- premature architecture expansion
- autonomous ticket chaining without boundaries

---

# Required Output

## Ticket Completed

```txt
PIP-X
```

---

## What Was Unblocked

Explain:

- new capabilities
- new possible tickets
- resolved dependencies

---

## Recommended Next Ticket

```txt
PIP-X
```

---

## Why This Ticket Is Next

Explain:

- dependency logic
- MVP rationale
- operational rationale

---

## GO Conditions

List conditions required to proceed.

---

## NO-GO Conditions

List blockers.

---

## Optional Dependencies

List placeholders/mocks/deferred integrations.

---

## Restrictions

Define what must not happen.

---

## Human Approval Requirement

Unless explicitly authorized, do not automatically continue execution.

Always:

- recommend
- explain
- wait

---

# Anti-Patterns

Avoid:

- infinite autonomous execution
- chaining unrelated tickets
- prioritizing production over MVP learning
- hidden roadmap changes
- expanding scope automatically
