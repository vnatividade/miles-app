#!/usr/bin/env python3
"""Soft-warning PreToolUse hook for risky command reminders.

This script is intentionally safe and non-blocking:
- no network access
- no file mutation
- no command mutation
- no secrets access
- no hard failures
- always exits 0

It can be wired to a future Codex PreToolUse hook to warn before risky
shell/tool operations. Runtime hooks remain disabled by default.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from typing import Any

SAFE_COMMAND_PATTERNS = [
    r"^\s*pytest\b",
    r"^\s*python\s+-m\s+pytest\b",
    r"^\s*ruff\s+check\b",
    r"^\s*mypy\b",
    r"^\s*git\s+status\b",
    r"^\s*git\s+diff\b",
    r"^\s*uv\s+sync\b",
    r"^\s*poetry\s+install\b",
    r"^\s*alembic\s+upgrade\s+head\b",
]

RISK_RULES = {
    "secrets / credentials": {
        "patterns": [
            r"\bcat\s+\.env\b",
            r"\bprintenv\b",
            r"\benv\b.*\b(KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL)\b",
            r"\.ssh/",
            r"\.aws/credentials",
            r"private[_-]?key",
            r"\bgrep\b.*\b(API_KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL)\b",
        ],
        "agents": ["risk_reviewer", "readiness_validator"],
        "message": "Potential secret or credential exposure. Confirm necessity and avoid printing or committing secrets.",
    },
    "production deploy / runtime mutation": {
        "patterns": [
            r"\brailway\s+(up|deploy)\b",
            r"\bkubectl\s+apply\b.*\b(prod|production)\b",
            r"\bterraform\s+apply\b",
            r"\bvercel\b.*\b--prod\b",
            r"\bfly\s+deploy\b",
            r"\bdeploy\b.*\b(prod|production)\b",
        ],
        "agents": ["risk_reviewer", "readiness_validator"],
        "message": "Potential production or runtime change. Confirm human approval before proceeding.",
    },
    "destructive database / data operation": {
        "patterns": [
            r"\bdrop\s+database\b",
            r"\btruncate\s+table\b",
            r"\bdelete\s+from\s+\w+\b",
            r"\balembic\s+downgrade\s+base\b",
            r"\bpsql\b.*\b(delete|drop|truncate)\b",
        ],
        "agents": ["risk_reviewer", "software_architect"],
        "message": "Potential destructive database or data operation. Confirm environment and approval.",
    },
    "billing / Stripe payment operation": {
        "patterns": [
            r"\bstripe\b.*\b(products|prices|checkout|subscriptions|payment)\b.*\b(create|update|delete|trigger)\b",
            r"\bcheckout\b.*\b(production|live|payment|subscription)\b",
            r"\bcharge\b.*\b(user|customer|card)\b",
            r"\blive[_-]?key\b",
        ],
        "agents": ["product_guardian", "billing_strategy_agent", "risk_reviewer"],
        "message": "Potential billing/payment operation. Confirm test mode, monetization strategy and human approval.",
    },
    "paid ads / budget spend": {
        "patterns": [
            r"\b(meta|facebook)\s+ads\b.*\b(create|launch|publish|activate)\b",
            r"\bcampaign\b.*\b(launch|publish|activate)\b",
            r"\bbudget\b.*\b(spend|daily|lifetime)\b",
            r"\bcreate_.*campaign\b",
            r"\blaunch[-_]?ads\b",
        ],
        "agents": ["product_guardian", "growth_experiment_agent", "risk_reviewer"],
        "message": "Potential paid acquisition action. Confirm budget cap and human approval.",
    },
    "risky provider scraping": {
        "patterns": [
            r"\b(scraper|scraping)\b.*\b(live|production|provider)\b",
            r"\bprovider\b.*\b(scraper|scraping|automation)\b",
            r"\banti[-_ ]?bot\b",
            r"\bcaptcha\b",
            r"\bbypass\b.*\b(captcha|anti[-_ ]?bot)\b",
        ],
        "agents": ["product_guardian", "risk_reviewer", "software_architect"],
        "message": "Potential risky provider automation. Confirm provider risk review and scope.",
    },
    "dangerous filesystem operation": {
        "patterns": [
            r"\brm\s+-rf\s+/\b",
            r"\brm\s+-rf\s+\.git\b",
            r"\bfind\b.*\b-delete\b",
            r"\bdelete\b.*\bproduction\b",
        ],
        "agents": ["risk_reviewer"],
        "message": "Potential destructive filesystem operation. Confirm intent before proceeding.",
    },
}


@dataclass(frozen=True)
class RiskMatch:
    category: str
    matched_patterns: list[str]
    agents: list[str]
    message: str


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


def _extract_command_text(payload: dict[str, Any]) -> str:
    possible_keys = [
        "command",
        "tool_input",
        "input",
        "args",
        "message",
        "raw_text",
    ]

    chunks: list[str] = []
    for key in possible_keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            chunks.append(value)
        elif isinstance(value, dict):
            try:
                chunks.append(json.dumps(value, ensure_ascii=False))
            except TypeError:
                pass

    if chunks:
        return "\n".join(chunks)

    try:
        return json.dumps(payload, ensure_ascii=False)
    except TypeError:
        return ""


def _is_safe_command(command_text: str) -> bool:
    return any(re.search(pattern, command_text, flags=re.IGNORECASE) for pattern in SAFE_COMMAND_PATTERNS)


def _find_risks(command_text: str) -> list[RiskMatch]:
    matches: list[RiskMatch] = []

    for category, rule in RISK_RULES.items():
        matched_patterns = [
            pattern
            for pattern in rule["patterns"]
            if re.search(pattern, command_text, flags=re.IGNORECASE | re.MULTILINE)
        ]
        if matched_patterns:
            matches.append(
                RiskMatch(
                    category=category,
                    matched_patterns=matched_patterns,
                    agents=list(rule["agents"]),
                    message=str(rule["message"]),
                )
            )

    return matches


def _print_no_risk() -> None:
    print("\n[Codex soft warning] PreToolUse risk check")
    print("No high-risk command pattern detected.")
    print("This is advisory only. It does not block execution.\n")


def _print_risks(matches: list[RiskMatch]) -> None:
    print("\n[Codex soft warning] Potential risky command detected")
    print("This is advisory only. It does not block execution.\n")

    for match in matches:
        print(f"Category: {match.category}")
        print(f"Message: {match.message}")
        print(f"Recommended agents: {', '.join(match.agents)}")
        print("Human approval may be required depending on environment and scope.")
        print()

    print("Recommended action:")
    print("- Confirm ticket scope and activation checks.")
    print("- Confirm whether human approval is required.")
    print("- Do not proceed with production, billing, paid ads, secrets or risky provider work without explicit approval.")
    print()


def main() -> int:
    raw_payload = _read_stdin()
    payload = _parse_payload(raw_payload)
    command_text = _extract_command_text(payload)

    if _is_safe_command(command_text):
        _print_no_risk()
        return 0

    matches = _find_risks(command_text)
    if matches:
        _print_risks(matches)
    else:
        _print_no_risk()

    # Soft-warning only. Never block Codex.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
