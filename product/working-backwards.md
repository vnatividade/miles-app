# Working Backwards Brief — miles-app

## Purpose

Clarify the product promise, strategic narrative, assumptions, risks and validation metrics for miles-app before expanding the MVP scope.

This document should guide product, frontend, backend and agentic execution.

---

# Press Release Draft

## Miles-app helps mileage travelers stop manually hunting flight redemptions

### Automated mileage alerts for people who want to find valuable flight opportunities before they disappear.

**Brazil, MVP stage** — miles-app is a monitoring product for people who use airline mileage programs and want to find relevant redemption opportunities without manually checking multiple programs every day.

Users configure alerts by origin, destination, date range, cabin, maximum miles, maximum cash fee and preferred programs. The system periodically monitors supported mileage programs, stores results, matches opportunities against user preferences and sends notifications when relevant options appear.

---

# Problem

Mileage users often need to manually check multiple airline or loyalty program websites to find good redemptions.

This is painful because:

- good opportunities disappear quickly
- mileage prices vary a lot
- fees and date availability change frequently
- checking manually is repetitive and time-consuming
- users often do not know whether they missed a better opportunity

---

# Target Customer

Initial target users:

- people who already use airline miles or loyalty programs
- people who travel at least occasionally and care about optimizing redemption value
- people willing to configure route/date alerts
- people who currently monitor programs manually or follow deal channels

Early adopter profile:

```txt
A mileage-aware traveler who already understands that good award availability is volatile and is willing to trust automated monitoring if notifications are relevant.
```

---

# Who This Is Not For

Not initially for:

- people who do not use miles
- people who want automatic ticket issuing
- people who need full travel agency support
- people who want complex mileage strategy consulting
- people who only travel with cash tickets

---

# Why Now

Several conditions make this product timely:

- mileage redemptions are increasingly dynamic
- users already expect alerts and automation in financial/travel products
- airline program pages are fragmented and time-consuming to monitor manually
- AI/automation tools reduce the cost of monitoring and matching opportunities
- solo/agentic execution enables a focused MVP before heavy platform investment

---

# How It Works

## 1. User creates an alert

The user configures:

- origin
- destination or destination region
- date range
- maximum miles
- maximum cash fee
- cabin class
- preferred programs
- notification channel

## 2. miles-app monitors programs

The system periodically searches supported mileage programs and stores raw and normalized results.

## 3. miles-app matches opportunities

Results are matched against user alert criteria.

## 4. User receives a notification

When a relevant opportunity appears, the user receives a notification with enough detail to decide whether to act.

## 5. User gives lightweight feedback

The user can mark an opportunity as useful or not useful, helping improve future matching and product direction.

---

# Differentiation

miles-app should not compete as a generic travel search engine.

The initial differentiation is:

```txt
persistent personalized monitoring for mileage redemption intent
```

Instead of asking users to search again and again, the product remembers what they care about and monitors continuously.

Potential future defensibility:

- user alert intent data
- route/provider performance history
- feedback on opportunity usefulness
- learned thresholds for relevance
- operational memory of provider behavior

---

# Benefits

## User Benefits

- less manual checking
- faster awareness of relevant opportunities
- better chance of catching volatile availability
- personalized alerts instead of generic deal noise
- simple feedback loop to improve relevance

## Product Benefits

- measurable retention through active alerts
- measurable value through useful opportunity feedback
- clear path to paid plans if users trust the monitoring

---

# Core Behavior Change

From:

```txt
I manually check airline mileage sites whenever I remember.
```

To:

```txt
I configure alerts and trust miles-app to notify me when something relevant appears.
```

---

# Primary Hypothesis

Users who already care about mileage redemptions will keep alerts active if miles-app finds opportunities that feel relevant enough to reduce manual search behavior.

---

# Validation Metrics

## North Star

```txt
Active alerts retained over time
```

## Activation

- first alert created
- alert has complete route/date/threshold criteria
- notification channel enabled

## Value Delivery

- matching opportunities found
- notifications sent
- useful opportunity feedback
- click/open rate on notifications

## Retention

- alerts active after 7 days
- alerts active after 30 days
- users creating additional alerts
- users returning after notification

## Qualitative Signals

- users say they currently check manually
- users can describe a recent missed or painful redemption search
- users accept imperfect MVP monitoring
- users ask for more routes/programs
- users say they would pay to keep alerts running

---

# Strategic FAQ

## 1. What problem are we solving?

Manual monitoring of mileage redemption opportunities across fragmented airline/loyalty programs.

## 2. Is the problem frequent?

Hypothesis: frequent for mileage-aware travelers who are actively planning trips or watching specific routes.

Needs customer discovery validation.

## 3. Is the problem painful enough?

Hypothesis: painful when users care about specific dates/routes and know opportunities are volatile.

Needs validation through interviews and alert retention.

## 4. What does success look like?

Users keep alerts active because they believe the system reduces manual checking and finds relevant opportunities.

## 5. What is the MVP?

A backend/API capable of storing alerts, monitoring initial supported programs, matching results and notifying users by email.

## 6. What is explicitly not the MVP?

- automatic ticket issuing
- payments
- full travel planning
- airline account integration
- mobile app
- broad multi-provider support
- AI travel assistant

## 7. Why start with alerts?

Alerts capture user intent and create a measurable retention loop.

## 8. Why not start with a full dashboard?

A dashboard may improve experience, but the validation question is whether users trust automated monitoring enough to keep alerts active.

## 9. What is hard to copy later?

Initially, not much. Future defensibility must come from accumulated user intent, feedback, provider behavior history and execution reliability.

## 10. What could kill this idea?

- providers block scraping aggressively
- users do not trust automated results
- opportunities are not meaningfully better than existing deal channels
- notifications are noisy or irrelevant
- users want consulting rather than software
- legal/compliance risk around scraping becomes unacceptable

## 11. What must be learned before scaling?

- which users care enough
- which routes create value
- which programs are technically feasible
- what users consider a good opportunity
- whether email alerts are sufficient
- whether users would pay

---

# Key Assumptions

| Assumption | Validation Path |
|---|---|
| Users manually check mileage programs today | Customer discovery interviews |
| Users want personalized alerts | Alert creation and retention |
| Useful opportunities can be captured reliably | Scraper success rate and result quality |
| Users trust email notifications | Open/click/usefulness metrics |
| Users will tolerate initial limited providers | MVP usage and feedback |
| Users may pay if alerts are valuable | Interviews, waitlist, pricing tests later |

---

# Risks

## Product Risks

- users may prefer manual search or deal communities
- alert configuration may feel too complex
- relevance may be hard to define universally
- limited providers may reduce perceived value

## Technical Risks

- scraping instability
- provider layout changes
- throttling or blocking
- noisy/duplicated results
- persistence model too rigid for provider differences

## Operational Risks

- too many alerts without enough monitoring capacity
- weak observability on scraper failures
- lack of clear incident process for provider failures

## Legal/Compliance Risks

- terms of service constraints
- potential restrictions around automated access
- data handling if user accounts are ever integrated

---

# MVP Guardrails

Build only what helps validate:

```txt
Do users trust automated mileage monitoring enough to keep alerts active?
```

Defer anything that does not improve that learning loop.

---

# Immediate Product Questions

- Which user segment should be interviewed first?
- What route/date patterns should initial alerts support?
- What is the minimum useful provider coverage?
- What opportunity threshold feels valuable?
- How much notification noise is acceptable?
- Would users pay for monitoring or only for successful findings?

---

# Next Recommended Actions

1. Run customer discovery interviews.
2. Use MVP scope review before expanding features.
3. Validate backend alert model against real user intent language.
4. Use Lovable only to prototype alert creation and opportunity feedback flows.
5. Keep scraper work focused on proving monitoring feasibility, not broad provider coverage.
