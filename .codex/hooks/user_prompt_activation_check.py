#!/usr/bin/env python3
"""Soft-warning UserPromptSubmit hook for activation reminders.

This script is intentionally safe and non-blocking:
- no network access
- no file mutation
- no secrets access
- no hard failures
- always exits 0

It can be wired to a future Codex UserPromptSubmit hook to remind agents
about ticket IDs, ticket types, activation checks and approval-gated language
before execution starts.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from typing import Any

TICKET_PATTERN = re.compile(r"\bPIP-\d+\b", re.IGNORECASE)

TICKET_TYPES = [
    "product",
    "backend",
    "frontend",
    "infra",
    "observability",
    "research",
    "growth",
    "billing",
    "scraper/provider",
    "scraper",
    "provider",
    "risk/security",
    "risk",
    "security",
    "documentation",
    "architecture",
    "knowledge",
]

APPROVAL_GATED_RULES = {
    "production/deploy": ["production", "prod", "deploy", "railway"],
    "secrets/config": ["secret", "secrets", "credential", "token", ".env"],
    "billing/stripe": ["stripe", "checkout", "subscription", "payment", "charge", "billing"],
    "paid growth": ["paid ads", "ads", "campaign", "budget", "meta ads", "facebook ads"],
    "scraper/provider risk": ["scraper", "scraping", "provider", "anti-bot", "captcha"],
    "autonomous continuation": ["continue automatically", "auto continue", "next ticket automatically"],
}

RECOMMENDED_AGENTS = {
    "production/deploy": ["risk_reviewer", "readiness_validator"],
    "secrets/config": ["risk_reviewer", "readiness_validator"],
    "billing/stripe": ["product_guardian", "billing_strategy_agent", "risk_reviewer"],
    "paid growth": ["product_guardian", "growth_experiment_agent", "risk_reviewer"],
    "scraper/provider risk": ["product_guardian", "risk_reviewer", "software_architect"],
    "autonomous continuation": ["roadmap_orchestrator"],
}


@dataclass(frozen=True)
class PromptReview:
    has_ticket_id: bool
    has_ticket_type: bool
    detected_ticket_types: list[str]
    approval_gated_matches: dict[str, list[str]]


def _read_stdin() -> str:
    try:
        return sys.stdin.read()
    except Exception:
        return ""


def _parse_payload(raw_payload: str) -> dict[str, Any]:
    if not raw_payload.strip():
        return {}

    try:
        parsed = json.loads(raw_payload)
    except json.JSONDecodeError:
        return {"raw_text": raw_payload}

    return parsed if isinstance(parsed, dict) else {"payload": parsed}


def _extract_prompt_text(payload: dict[str, Any]) -> str:
    possible_keys = ["prompt", "message", "text", "input", "raw_text"]

    for key in possible_keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value

    try:
        return json.dumps(payload, ensure_ascii=False)
    except TypeError:
        return ""


def _detect_ticket_types(text: str) -> list[str]:
    normalized = text.lower()
    detected: list[str] = []

    for ticket_type in TICKET_TYPES:
        if ticket_type in normalized:
            detected.append(ticket_type)

    return sorted(set(detected))


def _detect_approval_gated_language(text: str) -> dict[str, list[str]]:
    normalized = text.lower()
    matches: dict[str, list[str]] = {}

    for category, keywords in APPROVAL_GATED_RULES.items():
        found = [keyword for keyword in keywords if keyword in normalized]
        if found:
            matches[category] = found

    return matches


def _review_prompt(text: str) -> PromptReview:
    detected_ticket_types = _detect_ticket_types(text)

    return PromptReview(
        has_ticket_id=bool(TICKET_PATTERN.search(text)),
        has_ticket_type=bool(detected_ticket_types),
        detected_ticket_types=detected_ticket_types,
        approval_gated_matches=_detect_approval_gated_language(text),
    )


def _print_review(review: PromptReview) -> None:
    print("\n[Codex soft warning] UserPromptSubmit activation reminder")
    print("This is advisory only. It does not block execution.\n")

    if not review.has_ticket_id:
        print("- No PIP ticket ID detected. Confirm there is a Linear ticket before execution.")

    if not review.has_ticket_type:
        print("- No ticket type detected. Classify the ticket using execution/ticket-type-activation-matrix.md.")
    else:
        print("- Detected possible ticket type(s): " + ", ".join(review.detected_ticket_types))

    if review.approval_gated_matches:
        print("\nPotential approval-gated language detected:")
        for category, keywords in review.approval_gated_matches.items():
            agents = RECOMMENDED_AGENTS.get(category, [])
            print(f"- {category}: {', '.join(keywords)}")
            if agents:
                print(f"  Recommended agents: {', '.join(agents)}")
        print("\nConfirm human approval requirements before execution.")

    print("\nRecommended preflight shape:")
    print("""
Primary ticket type:
Secondary ticket types:
Activation triggers:
Required agents:
Required skills:
Approval-gated actions:
Human approval required: Yes/No
Decision: proceed / constrain / split / defer / block
""".strip())
    print()


def main() -> int:
    raw_payload = _read_stdin()
    payload = _parse_payload(raw_payload)
    prompt_text = _extract_prompt_text(payload)
    review = _review_prompt(prompt_text)
    _print_review(review)

    # Soft-warning only. Never block Codex.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
