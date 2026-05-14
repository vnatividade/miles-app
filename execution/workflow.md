# Execution Workflow — miles-app

## Purpose

Define how work must move from product rationale to executable tickets, implementation, review, and handoff.

The goal is to ensure that any AI agent or human contributor can understand:

- what needs to be done
- why it matters
- which agent gates apply
- what has already been completed
- what remains pending
- how to continue the work safely

---

# Source of Truth

## Repository

The repository is the source of truth for:

- product vision
- PRD
- architecture
- technical decisions
- execution rules
- agent activation rules
- done criteria
- handoff protocol

## Linear

Linear is the source of truth for:

- tickets
- status
- priorities
- milestones
- ownership
- execution visibility
- operational progress

---

# Standard Flow

```txt
Product Context
→ Architecture Context
→ Agent Activation Check
→ Ticket Creation / Selection
→ Preflight Review
→ Ticket Execution
→ Pull Request
→ Review
→ Done
→ Handoff
→ Roadmap Recommendation
```

---

# Required Steps Before Execution

Before implementing anything, the agent must:

1. Read relevant product documents.
2. Read relevant architecture documents.
3. Read `execution/product-agent-pipeline.md`.
4. Check existing tickets in Linear.
5. Create or select one ticket.
6. Confirm the ticket has clear scope.
7. Confirm acceptance criteria.
8. Identify required agent activations.
9. Run or document required preflight reviews.
10. Confirm whether human approval is required.
11. Create or use an appropriate branch.
12. Execute only the ticket scope.

---

# Agent Activation Check

For every ticket, the agent must identify:

```txt
Activation Trigger:
Required Agent:
Required Skill:
Mode:
Expected Output:
Human Approval Required:
```

Use:

```txt
execution/product-agent-pipeline.md
```

as the governing reference.

---

# Required Product Preflight

The Product Guardian must run before tickets involving:

- new product behavior
- user-facing feature work
- frontend/Lovable flow changes
- alert behavior
- opportunity display
- feedback capture
- notification behavior
- provider/scraper expansion
- billing/Stripe
- pricing
- organic growth
- paid ads

Required output:

```txt
Decision: Approve | Approve With Constraints | Defer | Split Ticket | Reject | Escalate For Human Approval
```

---

# Human Approval Gates

Agents must stop before:

- production deployment
- production secrets
- real user charging
- billing activation
- paid ads launch
- major product pivot
- risky scraping/provider automation
- autonomous continuation into another ticket

The agent may prepare a plan, but must not execute approval-gated actions without explicit human approval.

---

# Required Steps After Execution

After executing a ticket, the agent must:

1. Update or propose ticket status update.
2. Document what changed.
3. Document files changed.
4. Document pending items.
5. Open or update a pull request.
6. Add handoff notes for the next agent.
7. Update repository documentation if a structural decision was made.
8. Run or invoke roadmap_orchestrator.
9. Recommend the next logical ticket.
10. State whether human approval is required before continuing.

---

# Ticket Status Flow

```txt
TODO
→ READY
→ IN_PROGRESS
→ IN_REVIEW
→ DONE
→ HANDOFF_READY
```

---

# Execution Rule

No agent should implement work without a ticket.

If no ticket exists, the agent must create one before starting.

---

# Scope Control

Each ticket should be small enough to be completed independently.

Avoid tickets that mix:

- product decisions
- architecture changes
- implementation
- tests
- deployment
- research
- growth execution
- billing activation

Break them into separate tickets when needed.

---

# Pull Request Handoff

Every PR must include:

- Linear ticket reference
- context
- included scope
- excluded scope
- activation checks performed
- risks
- completed work
- pending work
- suggested next ticket

---

# Important Rule

The workflow should make future execution possible without conversational memory.
