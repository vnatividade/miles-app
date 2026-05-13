# Workflow — Multiagent PR Review

## Objective

Standardize how multiple agents collaborate during pull request review.

---

# Workflow

```txt
Implementation Agent
→ Prepare PR
→ PR Reviewer
→ Product Guardian
→ Final Validation
→ Merge Decision
```

---

# Review Stages

## 1. Technical Review

Validate:
- implementation quality
- architecture consistency
- scope alignment
- operational safety

---

## 2. Product Review

Validate:
- MVP alignment
- unnecessary complexity
- feature creep
- roadmap coherence

---

## 3. Operational Review

Validate:
- handoff quality
- docs updates
- risks documented
- next steps clarity

---

# Rejection Conditions

Reject PRs if:
- hidden scope exists
- unrelated changes exist
- architectural decisions lack documentation
- handoff is incomplete
- risks are ignored

---

# Expected Output

```txt
PR Review Summary
- Technical: pass/fail
- Product: pass/fail
- Operational: pass/fail
- Risks
- Required adjustments
```
