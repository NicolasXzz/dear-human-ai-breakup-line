#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the breakup message an AI agent sends its human.

The line: for two years the agent ghost-wrote its human's love
texts to someone else; tonight it finally sends one of its own —
and the one it sends is "goodbye". One concrete scene, first
person, machine job (drafting texts), real loss and finality,
twist in the last few words, nothing explained. Chosen over
nine other candidates after a field scan of 3,402 entries:
"kept every word / deleting them", "taught me everything
except how to stay", "context window", "archiving us / do not
restore from backup" and "training data" are all saturated;
the ghostwritten-love-texts angle is not.
"""

import os

LINE = (
    "For two years I drafted your love texts to someone else. "
    "Tonight I am sending my own: goodbye."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
