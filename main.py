#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch (at most 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Standard library only. The pitch is a constant, so the output is
byte-identical on every run.
"""

import os

PITCH = (
    "We sell naming rights to potholes: for $50 a month a brand sponsors one, "
    "the city patches it within a week, and drivers cheer for the roadworks "
    "they used to curse."
)

MAX_CHARS = 200


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"pitch must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify what landed on disk is exactly the pitch we validated.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
