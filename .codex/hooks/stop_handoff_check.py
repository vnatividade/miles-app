#!/usr/bin/env python3
"""Soft-warning Stop hook for Codex handoff reminders.

This script is intentionally safe and non-blocking:
- no network access
- no file mutation
- no secrets access
- no hard failures
- always exits 0

It can be wired to a future Codex Stop hook to remind agents to include
required handoff fields after task execution.
"""

from __future__ import annotations

import json
import sys
from typing import Any

REQUIRED_HANDOFF_FIELDS = [
    "Activation checks performed",
    "Files changed",
    "Tests/checks run",
    "Risks",
    "Pending items",
    "Suggested next ticket",
    "Human approval required before continuing",
]


def _read_stdin() -> str:
    """Read stdin safely.

    Codex hook payloads may vary by environment/version. This script treats
    stdin as optional and never fails when the payload is missing or invalid.
    """
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


def _extract_text(payload: dict[str, Any]) -> str:
    """Extract best-effort text from a hook payload."""
    possible_keys = [
        "message",
        "prompt",
        "response",
        "transcript",
        "text",
        "raw_text",
    ]

    for key in possible_keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value

    try:
        return json.dumps(payload, ensure_ascii=False)
    except TypeError:
        return ""


def _missing_fields(text: str) -> list[str]:
    normalized = text.lower()
    return [field for field in REQUIRED_HANDOFF_FIELDS if field.lower() not in normalized]


def _print_reminder(missing_fields: list[str]) -> None:
    print("\n[Codex soft warning] Handoff reminder")
    print("This is advisory only. It does not block execution.\n")

    if missing_fields:
        print("Consider including these handoff fields before finishing:")
        for field in missing_fields:
            print(f"- {field}")
    else:
        print("Required handoff fields appear to be present.")

    print("\nRecommended handoff shape:")
    print("""
Activation checks performed:
Files changed:
Tests/checks run:
Risks:
Pending items:
Suggested next ticket:
Human approval required before continuing:
""".strip())
    print()


def main() -> int:
    raw_payload = _read_stdin()
    payload = _parse_payload(raw_payload)
    text = _extract_text(payload)
    missing_fields = _missing_fields(text)
    _print_reminder(missing_fields)

    # Soft-warning only. Never block Codex.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
