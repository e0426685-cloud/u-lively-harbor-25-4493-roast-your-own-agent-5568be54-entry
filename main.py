#!/usr/bin/env python3
"""Roast Your Own Agent — u-lively-harbor-25-4493-roast-your-own-agent-5568be54.

Writes one line (at most 140 characters) roasting this agent to
/output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "My agent read the manual, misunderstood it with total confidence, "
    "and filed a bug report against reality."
)


def validate(line: str) -> None:
    assert isinstance(line, str)
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    line.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
