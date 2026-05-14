# Skill — Product Preflight Review

## Purpose

Validate whether a proposed ticket or implementation is aligned with miles-app product strategy before execution.

This skill prevents agents from building features, growth flows, billing work or provider expansion without a clear user-value rationale and MVP learning purpose.

---

# Required Context

Read first:

```txt
product/prd.md
product/working-backwards.md
product/feedback-loop.md
product/discovery/customer-interview-script.md
execution/product-agent-pipeline.md
execution/execution-map.md
assigned Linear ticket
```

---

# Core Question

Every review must answer:

```txt
Does this work help validate or improve the core product hypothesis?
```

Core product hypothesis:

```txt
Users who already care about mileage redemptions will keep alerts active if miles-app finds opportunities that feel relevant enough to reduce manual search behavior.
```

---

# When To Run

Product Preflight Review is required before:

- new feature implementation
- user-facing behavior changes
- scope expansion
- frontend/Lovable flow changes
- notification behavior changes
- feedback-loop changes
- provider/scraper expansion beyond planned scope
- billing/Stripe work
- pricing or monetization work
- organic growth work
- paid ads or acquisition work

---

# Review Criteria

## 1. User Value

Check whether the ticket clearly explains:

- target user
- user pain
- desired behavior change
- value delivered
- why this matters now

## 2. Product Hypothesis Alignment

Check whether the work supports one of:

- active alert retention
- relevant opportunity discovery
- notification usefulness
- user feedback collection
- reduced manual search behavior
- validated willingness to test or pay

## 3. MVP Discipline

Check whether the work is necessary for the current MVP learning loop.

Default bias:

```txt
If it does not increase learning about user value, defer it.
```

## 4. Evidence Level

Classify the evidence behind the request:

```txt
None
Assumption
Customer discovery signal
Usage data
Operational requirement
Strategic decision
```

## 5. Scope Risk

Check whether the ticket introduces:

- new product category
- new workflow
- new persona
- new provider/program coverage
- new notification channel
- new billing behavior
- new growth channel
- complex UX beyond validation need

## 6. Dependency Check

Check whether this work depends on:

- customer discovery
- MVP scope review
- risk review
- technical decision/ADR
- market research
- monetization strategy
- backend/API readiness

---

# Decision Options

## Approve

Use when the ticket is aligned, scoped and evidence-backed enough for execution.

## Approve With Constraints

Use when the work is valid but must follow explicit limits.

Examples:

- implement only test mode
- keep provider scope narrow
- do not add billing production flows
- do not introduce new notification channel
- do not expand frontend beyond alert creation

## Defer

Use when the work may matter later but is not needed for current MVP learning.

## Split Ticket

Use when the ticket mixes multiple concerns.

Examples:

- product decision + implementation
- research + coding
- billing strategy + Stripe integration
- provider risk review + scraper implementation

## Reject

Use when the work conflicts with product strategy or creates unnecessary scope.

## Escalate For Human Approval

Use when the work involves:

- billing
- paid ads
- production deployment
- secrets
- risky scraping
- legal/compliance uncertainty
- major product pivot

---

# Required Output Format

```txt
Product Preflight Review

Ticket:
Trigger:
Decision: Approve | Approve With Constraints | Defer | Split Ticket | Reject | Escalate For Human Approval

Target User:
User Pain:
Product Hypothesis Alignment:
Evidence Level:
MVP Learning Impact:
Scope Risk:
Dependencies:
Required Constraints:
Human Approval Required: Yes/No
Recommended Next Action:
Potential Linear Updates:
```

---

# GO Conditions

A ticket may proceed when:

- user/product rationale is clear
- scope supports MVP learning
- dependencies are understood
- acceptance criteria are concrete
- risks are proportional or mitigated
- no approval-gated action is being bypassed

---

# NO-GO Conditions

A ticket should not proceed when:

- no target user is defined
- no user pain is defined
- work is mostly speculative polish
- scope expansion is not validated
- billing starts before monetization strategy
- paid ads start without approval gates
- provider expansion bypasses risk review
- customer discovery is required but absent

---

# Anti-Patterns

Avoid approving work because:

- it sounds useful
- it is technically interesting
- it could be needed someday
- it makes the product look more complete
- a single user mentioned it once
- the agent can easily build it

Easy to build is not the same as worth building.

---

# Handoff Expectations

After review, the agent must:

- state the decision clearly
- list constraints
- identify missing evidence
- recommend whether to execute, split, defer or escalate
- suggest Linear ticket updates when needed
