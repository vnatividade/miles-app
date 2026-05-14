# Customer Discovery Script — miles-app

## Purpose

Validate whether mileage-aware travelers have a real, frequent and painful problem with manually monitoring mileage redemption opportunities.

This script should help us learn before expanding product scope, billing, paid acquisition or provider coverage.

---

# Core Hypothesis

```txt
Users who already care about mileage redemptions will keep alerts active if miles-app finds opportunities that feel relevant enough to reduce manual search behavior.
```

---

# What We Need To Learn

## Problem

- Do users actively monitor mileage programs today?
- How often do they monitor?
- What makes the process painful?
- What do they do when they miss a good opportunity?

## Current Alternatives

- Do they use airline sites directly?
- Do they follow deal communities?
- Do they use spreadsheets, reminders or Telegram/WhatsApp groups?
- Do they use paid services or consultants?

## Value

- Would they trust automated monitoring?
- What would make an alert useful?
- What level of false positive/noise is acceptable?
- Would they pay to keep monitoring running?

## MVP Scope

- Which routes/programs matter first?
- Is email enough as the first notification channel?
- What information must a notification include?
- What should not be built yet?

---

# Target Personas

## Primary Persona — Mileage-Aware Traveler

People who already use miles and understand that availability and pricing are volatile.

Signals:

- knows at least one mileage program
- has searched for award tickets before
- cares about route/date/miles thresholds
- understands that good opportunities can disappear

## Secondary Persona — Deal Follower

People who follow mileage/promo channels but do not actively search every day.

Signals:

- follows Instagram, Telegram, WhatsApp or blogs about travel deals
- wants opportunities but may not know exact rules
- may prefer curated alerts over advanced configuration

## Not Initial Persona — Beginner Traveler

People who do not use miles yet.

Reason:

```txt
Education-heavy users may require a different product: content, consulting or guided planning.
```

---

# Interview Format

Recommended duration:

```txt
20 to 30 minutes
```

Recommended sample:

```txt
5 to 10 interviews before changing MVP direction
```

Interview mode:

- conversation first
- avoid selling the solution too early
- ask about real past behavior
- ask for specific examples
- avoid hypothetical enthusiasm traps

---

# Interview Opening

Use this opener:

```txt
I am exploring how people find good flight redemptions with miles. I am not trying to sell anything right now. I want to understand how you currently search, what is painful and what would actually be useful.
```

---

# Section 1 — Qualification

## Questions

1. Which mileage or loyalty programs do you currently use?
2. When was the last time you tried to issue a flight using miles?
3. What route or destination were you looking for?
4. Did you actually issue the ticket? Why or why not?
5. How comfortable are you with searching award availability?

## Strong Signals

- user gives specific program names
- user remembers routes and dates
- user describes difficulty finding good availability
- user has repeated this process more than once

## Weak Signals

- user talks only about wanting to travel someday
- user has never searched for award availability
- user does not understand mileage redemption basics

---

# Section 2 — Current Behavior

## Questions

1. Walk me through the last time you searched for a flight with miles.
2. Which sites or apps did you open?
3. How many times did you check before deciding?
4. Did you compare multiple dates or programs?
5. Did you use any group, newsletter, Instagram profile, Telegram channel or consultant?
6. Did you save the results somewhere?

## Follow-Ups

- What was annoying about that process?
- What took more time than expected?
- What information was missing?
- Did you feel confident you found the best option?

## Strong Signals

- repeated manual checking
- checking multiple programs/dates
- fear of missing better availability
- dependence on external deal communities
- frustration with volatility

---

# Section 3 — Pain Intensity

## Questions

1. What happens when you do not find a good redemption?
2. Have you ever missed an opportunity because you saw it too late?
3. How often do you think prices or availability change?
4. How much time do you usually spend searching?
5. If you had to give this problem a score from 1 to 10, how painful is it?

## Follow-Ups

- Why that score?
- What would make it a 10?
- What would make it not worth solving?

## Strong Signals

- user has missed opportunities before
- user checks repeatedly during trip planning
- user describes emotional frustration or opportunity cost
- user spends meaningful time searching

## Weak Signals

- user says it is annoying but rarely searches
- user would only use it if free
- user has no specific recent example

---

# Section 4 — Alert Concept Validation

Introduce the concept only after understanding current behavior.

## Concept Prompt

```txt
Imagine you could configure an alert saying: I want to leave from this airport, go to this destination or region, within this date range, paying up to this number of miles and fees. Then the system monitors programs and notifies you when something relevant appears.
```

## Questions

1. Would this have helped in your last search?
2. What exact alert would you create today?
3. Which origin, destination and date range would you configure?
4. What would be your maximum miles threshold?
5. What fees would be acceptable?
6. Which programs should be monitored first?
7. How quickly would you need to be notified?

## Strong Signals

- user immediately describes a real alert
- user knows specific route/date/program criteria
- user says this would replace manual checking
- user asks when it will exist

## Weak Signals

- user only says "interesting"
- user cannot define any alert
- user wants broad travel inspiration rather than monitoring

---

# Section 5 — Notification Usefulness

## Questions

1. What would make a notification useful?
2. What information must be included?
3. Would email be enough initially?
4. Would WhatsApp, Telegram or push be more valuable?
5. How many alerts would be too many?
6. What would make you turn off notifications?

## Required Notification Data To Test

Ask the user to rank importance:

- program
- origin
- destination
- date
- miles required
- cash fees
- cabin
- stops
- availability confidence
- booking link
- time found

---

# Section 6 — Willingness To Pay

Do not ask directly too early.

## Questions

1. If this saved you manual checking during trip planning, how valuable would it be?
2. Would you expect this to be free, paid or freemium?
3. What would make it worth paying for?
4. Would you pay for active alerts, successful findings or advanced routes?
5. Have you paid for any travel/miles tool, course, community or consultant before?
6. If this worked for your next trip, what price would feel reasonable?

## Strong Signals

- user already pays for related tools/content/consulting
- user gives a concrete price range
- user connects value to a trip outcome
- user says they would pay to avoid missing opportunities

## Weak Signals

- user says they would only use it free
- user likes the idea but cannot define value
- user wants full consulting for software price

---

# Section 7 — MVP Boundaries

## Questions

1. What is the smallest version that would still be useful?
2. Which programs must be included first?
3. Which features are unnecessary at the beginning?
4. Would you use it if only email alerts existed?
5. Would you use it if only Azul and Smiles were supported first?
6. Would you accept occasional missed opportunities if the system was transparent?

## Scope Signals

### Build Soon

- alert creation
- relevant notification
- opportunity usefulness feedback
- active alert retention

### Defer

- automatic ticket issuing
- payments before pricing validation
- mobile app
- complex dashboard
- AI travel assistant
- broad provider coverage

---

# Closing Questions

1. Is there anything I should have asked and did not?
2. Who else should I talk to about this?
3. Would you be willing to test an early version?
4. Can I contact you when the first version is ready?

---

# Interview Learning Output

For each interview, capture:

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

# Validation Signals

## Green Signals

- user has recent/manual search behavior
- user gives specific route/date/program examples
- user has missed opportunities before
- user would create an alert now
- user says alerts could replace manual checking
- user accepts limited MVP provider coverage
- user would test early version
- user shows willingness to pay or strong intent

## Yellow Signals

- user likes idea but has no immediate trip
- user wants broader inspiration, not monitoring
- user needs education before using alerts
- user wants WhatsApp/push before email

## Red Signals

- user does not search manually today
- user has no clear mileage behavior
- user would not trust automated monitoring
- user only wants free generic deal content
- user cannot define a useful alert
- user expects automatic ticket issuing as baseline

---

# Decision Rules

## If most users cannot describe recent manual monitoring

Revisit target persona.

## If users want inspiration instead of specific alerts

Consider whether product should pivot toward deal discovery/content rather than monitoring.

## If users create very specific alerts

Prioritize alert UX and matching quality.

## If users reject email

Reevaluate notification channel priority.

## If users tolerate limited providers

Keep provider scope narrow.

## If users demand automatic issuing

Clarify whether the MVP is insufficient or whether the target persona is wrong.

---

# Important Rule

Do not count compliments as validation.

Validation comes from:

```txt
specific past behavior
+
clear pain
+
concrete alert intent
+
willingness to test or pay
```
