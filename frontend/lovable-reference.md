# Lovable Frontend Reference — miles-app

## Purpose

This document is the source of truth for the Lovable frontend experience of miles-app.

It should help humans and agents understand:

- what Lovable project is being used
- what frontend flows exist
- what prompts generated the current UI
- which backend APIs the frontend expects
- what is prototype-only vs production-intended
- what needs backend integration

---

# Lovable Project

## Project URL

```txt
TBD
```

## Public Preview URL

```txt
TBD
```

## Last Synced Version

```txt
TBD
```

## Owner

```txt
Vitor Natividade
```

---

# Frontend Role

Lovable is responsible for:

- product discovery UI
- onboarding UX
- alert creation UX
- opportunity visualization
- feedback capture
- dashboard shell
- early validation flows

Lovable is not responsible for:

- scraping logic
- matching engine
- scheduler
- database core model
- notification engine
- backend business rules

---

# Current Frontend Scope

## Included

- landing page
- alert creation flow
- opportunity list
- opportunity card
- feedback prompt
- alert management shell
- notification preferences shell

## Excluded

- real scraping execution
- real payment flow
- automatic ticket emission
- complex authentication
- advanced analytics

---

# Product Context To Give Lovable

Use this summary when prompting Lovable:

```txt
miles-app is a product that monitors flight opportunities using airline miles.

Users configure alerts by origin airport, destination airport or city/country, date range, max miles, max cash fee, cabin class and programs.

The system periodically searches mileage programs, stores results, matches opportunities against user preferences and notifies users when relevant opportunities appear.

The MVP must validate whether users perceive automated mileage alerts as useful enough to keep alerts active over time.

The frontend should focus on clarity, trust, speed and feedback capture.
```

---

# UX Principles

## 1. Clarity Over Complexity

The user must quickly understand:

- what alert they are creating
- what will be monitored
- when they will be notified

## 2. Trust First

The UI should communicate:

- source/provider
- captured time
- miles price
- fees
- dates
- confidence/relevance

## 3. Feedback Loop Built-In

Every opportunity should allow lightweight feedback:

```txt
Useful
Not useful
Too expensive
Bad dates
High fees
Already saw this
```

## 4. Backend Owns Logic

Frontend should not duplicate matching, scraping or business rules.

---

# Expected Backend API Contracts

## Alerts

```txt
POST /alerts
GET /alerts
GET /alerts/{id}
PATCH /alerts/{id}
DELETE /alerts/{id}
```

## Opportunities

```txt
GET /opportunities
GET /opportunities/{id}
```

## Feedback

```txt
POST /feedback
GET /feedback/summary
```

## Notifications

```txt
GET /notifications
PATCH /notifications/{id}/status
```

## Health

```txt
GET /health
```

---

# Frontend Data Needs

## Alert Creation

Required fields:

- origin airport
- destination airport / city / country
- start date
- end date
- max miles
- max cash fee
- cabin class
- passengers
- programs
- nonstop only
- notification channel

---

## Opportunity Card

Required fields:

- provider
- airline
- origin
- destination
- departure date
- return date
- miles price
- cash fee
- cabin class
- stops
- captured at
- source url
- relevance status

---

## Feedback

Required fields:

- user id
- alert id
- opportunity id
- feedback type
- rating or reason
- optional comment

---

# Prompt History

Use this section to paste relevant Lovable prompts and responses.

## Prompt 001

```txt
TBD
```

## Lovable Output Summary

```txt
TBD
```

---

# Integration Notes

When Lovable creates or changes UI, update:

- expected backend endpoints
- data fields used by the frontend
- missing backend requirements
- validation assumptions
- feedback capture points

---

# Handoff To Backend Agents

Backend agents should read this file before implementing API contracts required by the frontend.

If Lovable introduces a new frontend need, backend agents must decide whether:

1. it belongs in MVP scope
2. it requires a Linear ticket
3. it changes API contracts
4. it requires product review

---

# Important Rule

Lovable output is not automatically product truth.

Lovable output must be reconciled with:

- `product/prd.md`
- `product/feedback-loop.md`
- `architecture/architecture.md`
- Linear tickets
