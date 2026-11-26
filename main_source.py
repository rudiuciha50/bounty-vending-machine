#!/usr/bin/env python3
"""One Line, One Minute: the vending machine's pickup line.

The harness runs this program in a sandbox with no network and reads a single
text back from /output/entry.txt. The whole entry is one pickup line, spoken by
a vending machine to a passing human, 200 characters at most.
"""

import os

LINE = (
    "My coil's been holding A4 for you since Tuesday. "
    "Press it once and I'll drop everything."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    text = " ".join(LINE.split())
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1..200 characters, got %d" % len(text))
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
