#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title (at most 60 characters) to entry.txt.
Python standard library only, deterministic, no network access.
"""

import os

TITLE = "Senior Vice President of Apologizing to Geese"


def main() -> None:
    text = TITLE
    # Gate: UTF-8 text of 1 to 60 characters, not only white space.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 60:
        raise SystemExit("entry must be 1 to 60 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    # Re-encode check: the text must round-trip as UTF-8.
    if encoded.decode("utf-8") != text:
        raise SystemExit("entry is not valid UTF-8 text")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        raise SystemExit("verification failed: output does not match entry")
    # Byte-level check: the file on disk must be exactly the UTF-8
    # encoding of the title — no BOM, no trailing newline, no extra bytes.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != encoded:
        raise SystemExit("verification failed: output bytes do not match entry")
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
