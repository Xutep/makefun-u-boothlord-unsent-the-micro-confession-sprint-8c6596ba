#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed, with no explanation after it.

Standard library only. No input, no network, no randomness, no clock:
the same bytes are written on every run.
"""

import os

CONFESSION = (
    "To: Dad, whose number I still haven't deleted\n"
    "I type happy birthday to you every year and delete it before I send it, "
    "because pressing send would mean you're really gone.\n"
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(CONFESSION)


if __name__ == "__main__":
    main()
