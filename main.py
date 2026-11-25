#!/usr/bin/env python3
"""Write one single-line office joke to entry.txt.

The competition gate requires UTF-8 text of 1-199 characters on a
single line. The joke lives in one constant so the program's only
job is to place it, unchanged, in the output directory.
"""

import os

JOKE = (
    "I replied-all to ask everyone to stop replying-all, and now "
    "47 people are agreeing with me in a thread called 'Please stop'."
)


def validate(text):
    """Enforce the competition gate before anything is written."""
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 199:
        raise ValueError("joke must be 1-199 characters, got %d" % len(text))


def main():
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(JOKE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
