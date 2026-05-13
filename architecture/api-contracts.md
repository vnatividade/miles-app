# API Contracts — miles-app

## Purpose

Define the initial backend API contracts required by the frontend MVP.

These contracts prevent frontend/backend drift while the MVP backend is still
being built incrementally.

---

# Contract Principles

## Backend Owns Business Logic

The frontend may render opportunities, alerts, feedback prompts and
notifications, but it must not implement scraping, matching, scheduling or
notification rules.

## Contract First, Implementation Incrementally

Some endpoints are implemented as placeholder contracts before persistence and
background jobs exist.

Placeholder endpoints must make their limitations explicit.

## MVP Scope

The initial contract prioritizes:

- alert creation and management
- opportunity display shape
- lightweight feedback capture
- notification list/status shape
- health checks

It intentionally excludes:

- authentication hardening
- production API versioning
- advanced pagination
- real scraping
- real matching
- real notification delivery

---

# Implemented Contracts

## Health

```txt
GET /health
```

Purpose:
- local/dev service health check

Status:
- implemented

---

## Alerts

```txt
POST /alerts
GET /alerts
GET /alerts/{id}
PATCH /alerts/{id}
DELETE /alerts/{id}
```

Purpose:
- create and manage user monitoring configurations

Status:
- implemented with SQLAlchemy persistence

Ownership:
- `user_id` is explicit until authentication and user principal resolution exist

Important request fields:

```txt
user_id
origin_airport
destination_airport
destination_city
destination_country
start_date
end_date
flexibility_days
cabin_class
passengers
max_miles
max_cash_fee
programs
nonstop_only
frequency_minutes
active
```

Validation highlights:

```txt
origin_airport and destination_airport are 3-character IATA codes
end_date must be on or after start_date
programs must contain at least one program
cabin_class must be economy, premium_economy, business or first
passengers must be between 1 and 9
frequency_minutes must be between 15 and 10080
```

Frontend note:
- notification channel is not stored on Alert yet
- notification preferences should remain a separate future contract

---

## Opportunities

```txt
GET /opportunities
GET /opportunities/{id}
```

Purpose:
- provide opportunity cards for the frontend MVP

Status:
- placeholder contract
- `GET /opportunities` returns an empty list until scraper, normalization and
  matching persistence exist
- `GET /opportunities/{id}` returns 404 until opportunity persistence exists

Response fields:

```txt
id
alert_id
provider
airline
origin
destination
departure_date
return_date
miles_price
cash_fee
currency
cabin_class
stops
flight_duration
availability
source_url
relevance_status
captured_at
```

Frontend note:
- `relevance_status` is backend-owned
- frontend should only render the status provided by the backend

---

## Feedback

```txt
POST /feedback
GET /feedback/summary
```

Purpose:
- support the MVP product learning loop

Status:
- placeholder contract
- `POST /feedback` accepts and echoes payloads but does not persist them yet
- `GET /feedback/summary` returns zero-state metrics until feedback persistence
  and analysis exist

Request fields:

```txt
user_id
alert_id
opportunity_id
feedback_type
rating
reason
comment
```

Supported feedback types:

```txt
alert_expectation
notification_relevance
alert_deactivation
weekly_pulse
manual_feedback
```

---

## Notifications

```txt
GET /notifications
PATCH /notifications/{id}/status
```

Purpose:
- allow frontend notification list and interaction states

Status:
- placeholder contract
- `GET /notifications` returns an empty list until notification persistence exists
- `PATCH /notifications/{id}/status` returns 404 until notification persistence
  exists

Response fields:

```txt
id
user_id
alert_id
opportunity_id
channel
status
sent_at
subject
```

Supported MVP channel:

```txt
email
```

Frontend-visible status updates:

```txt
opened
clicked
dismissed
```

---

# Frontend Dependency Map

## Alert Creation Flow

Backend status:
- supported by Alert API

Known gap:
- notification channel is not part of Alert persistence

Recommended follow-up:
- PIP-21 — Define notification preferences contract

---

## Opportunity List And Card

Backend status:
- contract shape exists
- real data not available yet

Known gaps:
- scraper execution not implemented
- normalized search result persistence not implemented
- matching engine not implemented

Recommended follow-ups:
- PIP-7 — Create scraper base contract
- PIP-19 — Implement opportunity persistence read model
- implement matching engine

---

## Feedback Capture

Backend status:
- request/response contract exists
- persistence not implemented

Known gap:
- UserFeedback persistence model does not exist

Recommended follow-up:
- PIP-20 — Implement feedback persistence model

---

## Notification Shell

Backend status:
- list and status contract exists
- notification delivery and persistence not implemented

Known gaps:
- notification provider setup not implemented
- notification history persistence not implemented

Recommended follow-ups:
- PIP-16 — Setup notification provider integration
- PIP-9 — Implement email notification provider
- implement notification history persistence

---

# PIP-18 Follow-Up Tickets

Recommended future tickets:

```txt
PIP-19 — Implement opportunity persistence read model
PIP-20 — Implement feedback persistence model
PIP-21 — Define notification preferences contract
Implement matching engine
Implement notification history persistence
```

Existing roadmap tickets that remain relevant:

```txt
PIP-7 — Create scraper base contract
PIP-9 — Implement email notification provider
PIP-16 — Setup notification provider integration
```
