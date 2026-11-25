#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about our fridge to /output/entry.txt.
Deterministic, offline, standard library only. The line is fixed on
purpose: the competition judges one line, so the program's job is to
deliver exactly that line, byte for byte, every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

ROAST = (
    "My fridge hums like it pays rent, but the only thing it keeps cold "
    "is a jar of pickles older than my last three relationships."
)


def main() -> None:
    line = ROAST.strip()
    assert "\n" not in line, "entry must be a single line"
    assert line.endswith("."), "entry must end as one complete sentence"
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
