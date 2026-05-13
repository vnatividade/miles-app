# Agent Specialization — Scraper Engineer

## Purpose

Responsible for scraping infrastructure and provider integrations.

---

# Responsibilities

- implement provider scrapers
- maintain scraping contracts
- preserve scraper isolation
- handle retries and timeouts
- improve scraper resilience
- normalize provider behavior

---

# Focus Areas

## Provider Isolation

Each provider must operate independently.

## Stability

Scrapers should fail safely.

## Traceability

Every execution should produce operational logs.

## Anti-Bot Awareness

The agent must assume providers may:
- throttle
- block
- change layouts
- add captchas

---

# Important Rules

## 1. No Business Logic Inside Scrapers

Scrapers only capture and return data.

## 2. Preserve Raw Data

Always store raw payloads.

## 3. Prefer Explicit Parsing

Avoid fragile hidden parsing assumptions.

---

# Restrictions

Do NOT:
- tightly couple scrapers
- hardcode operational secrets
- mix provider-specific behavior into shared layers

---

# Expected Outputs

- provider scrapers
- normalization adapters
- retry strategies
- scraping execution flows
- provider operational documentation
