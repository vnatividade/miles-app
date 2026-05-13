# CLAUDE.md — miles-app

## Project Purpose

miles-app is an automated monitoring platform for mileage-based flight opportunities.

The MVP focuses on:
- scraping
- normalization
- matching
- alerts

The system should help users discover mileage opportunities automatically.

---

# Required Reading Order

Before implementing anything, read:

```txt
product/
architecture/
execution/
agents/
Linear ticket
```

---

# Source of Truth

## Repository

The repository stores:
- product vision
- architecture
- workflows
- standards
- operational rules

## Linear

Linear stores:
- tickets
- milestones
- priorities
- operational progress

---

# Execution Rules

- Never execute work without a ticket.
- Work on one ticket scope at a time.
- Do not expand scope silently.
- Avoid unrelated modifications.
- Preserve MVP discipline.

---

# MVP Principles

Prefer:
- simple code
- explicit flows
- modularity
- operational traceability
- evolvable architecture

Avoid:
- premature optimization
- speculative abstractions
- enterprise complexity
- hidden coupling

---

# Scraper Principles

- providers must remain isolated
- preserve raw provider data
- expect anti-bot behavior
- avoid business logic inside scrapers

---

# Documentation Rules

Update documentation when:
- architecture changes
- workflows change
- contracts change
- operational behavior changes

---

# Pull Request Rules

Every PR must contain:
- ticket reference
- context
- scope included/excluded
- risks
- handoff notes
- suggested next ticket

---

# Important Rule

The next agent should never need to reverse engineer implementation reasoning.
