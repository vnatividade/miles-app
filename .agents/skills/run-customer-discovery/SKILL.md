# Skill — Run Customer Discovery

## Purpose

Guide agents and humans through customer discovery for miles-app.

This skill exists to validate whether the mileage alert problem is real, frequent and painful before expanding product scope, billing, paid acquisition or complex automation.

---

# Required Context

Read:

```txt
product/prd.md
product/feedback-loop.md
product/working-backwards.md
product/discovery/customer-interview-script.md
assigned Linear ticket
```

---

# Objective

Use customer interviews to validate:

- target persona
- manual monitoring behavior
- problem intensity
- current alternatives
- alert usefulness
- notification expectations
- willingness to test or pay
- MVP boundaries

---

# Interview Principles

## Ask About Past Behavior

Prioritize:

```txt
When was the last time you searched for a flight with miles?
```

Avoid relying on:

```txt
Would you use this someday?
```

---

## Do Not Sell Too Early

Understand current behavior before introducing the miles-app concept.

---

## Extract Specifics

Capture:

- programs used
- route searched
- date range
- miles threshold
- current workaround
- time spent
- missed opportunities
- willingness to test

---

## Separate Compliments From Validation

Compliments are weak evidence.

Strong evidence requires:

```txt
specific past behavior
+
clear pain
+
concrete alert intent
+
willingness to test or pay
```

---

# Required Workflow

## 1. Prepare

Define:

- interview goal
- target persona
- interview sample size
- strongest hypothesis to validate

---

## 2. Interview

Use:

```txt
product/discovery/customer-interview-script.md
```

Do not ask every question mechanically.

Follow the conversation while preserving the learning objective.

---

## 3. Capture Learnings

Use this format:

```txt
Interview ID:
Date:
Persona:
Mileage programs used:
Recent redemption search:
Current workaround:
Pain score:
Most painful moment:
Example alert they would create:
Notification preference:
Would test MVP:
Willingness to pay signal:
Strong quotes:
Risks/objections:
Product implications:
Potential Linear tickets:
```

---

## 4. Classify Signal

Classify each interview as:

```txt
Green
Yellow
Red
```

### Green

User shows real behavior, pain and concrete alert intent.

### Yellow

User likes the idea but evidence is incomplete.

### Red

User does not show the target behavior or would not trust/use alerts.

---

## 5. Synthesize

After 5 to 10 interviews, summarize:

- strongest signal
- weakest signal
- repeated objections
- route/program priorities
- MVP scope implications
- follow-up tickets
- whether to continue, pivot or pause

---

# Output Format

## Discovery Summary

```txt
Interview count:
Green signals:
Yellow signals:
Red signals:
Top personas:
Top pains:
Top current alternatives:
Top alert configurations:
Top notification preferences:
Willingness to pay signals:
MVP implications:
Risks:
Recommended Linear tickets:
Decision:
```

---

# Decision Options

## Continue

Enough evidence supports building the current MVP direction.

## Narrow

Evidence supports the problem but only for a narrower persona, route or provider.

## Pivot

Users have a real problem, but not the one currently framed.

## Pause

Evidence is too weak to justify more build.

---

# Anti-Patterns

Avoid:

- treating compliments as validation
- interviewing only friends who want to be nice
- pitching before learning
- asking hypothetical questions too early
- expanding scope based on one loud user
- building billing before validating willingness to pay

---

# Expected Outputs

- interview script usage
- interview notes
- signal classification
- discovery synthesis
- product implications
- suggested Linear tickets
