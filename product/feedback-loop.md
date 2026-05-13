# User Feedback Loop — miles-app

## Purpose

Define how miles-app will monitor whether the product is achieving its core objective and how user feedback will guide product evolution.

---

# Core Product Objective

The product succeeds when users keep alerts active because they believe the system helps them find relevant mileage flight opportunities.

The MVP must validate:

```txt
Users trust automated monitoring enough to stop manually checking mileage programs every day.
```

---

# Product North Star

## Primary Signal

```txt
Active alerts retained over time
```

This indicates that users still believe the system can generate value.

---

# Supporting Metrics

## Activation

Track:

- user created first alert
- user configured origin/destination/date range
- user defined max miles
- user opted into notifications

---

## Engagement

Track:

- active alerts
- alert edits
- viewed opportunities
- clicked notifications
- repeated visits
- saved routes

---

## Value Delivery

Track:

- opportunities found
- opportunities matching user criteria
- notifications sent
- notification open/click rate
- user marked opportunity as useful
- user marked opportunity as irrelevant

---

## Retention

Track:

- alerts still active after 7 days
- alerts still active after 30 days
- users creating additional alerts
- users returning after receiving notification

---

# Feedback Capture Moments

## 1. After Alert Creation

Ask:

```txt
What are you hoping to find with this alert?
```

Purpose:
- understand desired outcome
- validate route intent
- capture user expectation

---

## 2. After Notification

Ask:

```txt
Was this opportunity useful?
```

Possible answers:

```txt
Useful
Not useful
Too expensive in miles
Bad dates
High fees
Wrong destination
Already saw this
```

---

## 3. When User Deactivates Alert

Ask:

```txt
Why are you turning this alert off?
```

Possible answers:

```txt
I found a ticket
Results were not useful
Too many notifications
No longer traveling
Price was never good
I prefer manual search
Other
```

---

## 4. Weekly User Pulse

For active users, optionally ask:

```txt
Are your alerts still useful?
```

Purpose:
- detect silent dissatisfaction
- validate continued trust

---

# Feedback Data Model

Recommended entity:

```txt
UserFeedback
- id
- user_id
- alert_id
- search_result_id
- feedback_type
- rating
- reason
- comment
- created_at
```

---

# Feedback Types

```txt
alert_expectation
notification_relevance
alert_deactivation
weekly_pulse
manual_feedback
```

---

# Product Learning Loop

```txt
User Action
→ Feedback Capture
→ Data Storage
→ Product Analysis
→ Linear Ticket
→ Product/Algorithm Adjustment
→ Measurement
```

---

# Decision Rules

## If many opportunities are marked not useful

Review matching criteria and notification thresholds.

## If users deactivate alerts due to noise

Reduce notification frequency or improve relevance filtering.

## If users deactivate alerts after finding tickets

This is positive outcome data.

## If users keep alerts active but never click

Investigate notification content, channel and relevance.

## If users create multiple alerts

This indicates trust and potential willingness to pay.

---

# MVP Feedback Principle

Do not overbuild surveys.

Capture lightweight feedback at high-intent moments:
- alert creation
- notification received
- alert deactivation
- opportunity viewed

---

# Business Validation Questions

The feedback loop should help answer:

- Are users receiving opportunities they consider relevant?
- Are alerts reducing manual search behavior?
- Which providers/routes generate most value?
- Which alerts create frustration?
- What makes users keep or abandon the product?
- Which users would pay for this?

---

# Important Rule

A technically working scraper is not product success.

Product success means users perceive the alerts as useful enough to keep using the system.
