"""The Vacuum's Alibi: one line, 200 characters or fewer.

The robot vacuum explains why it missed a spot. The angle is a formal
court order: the vacuum did not fail to clean the spot — the dust won a
restraining order under statute 12-C, the sock was seized as exhibit A,
and cleaning is banned within 500 m of the scene. The line reads like a
docket entry, not a story: case number first, statute and evidence in
the middle, ruling code last. A deadpan machine cites the order and
stops — the ruling, not an apology, is the punchline.
"""

import os
import sys

TEXT = "ORDER #4471: dust v. VAC-2147 — restraining order granted, statute 12-C, sock seized as exhibit A, cleaning banned within 500 m. RULING: CASE CLOSED."


def main() -> int:
    """Write the alibi line to the harness output file and verify it."""
    if not TEXT or not TEXT.strip():
        print("gate failed: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"gate failed: entry is {len(TEXT)} characters, over 200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: written entry does not match TEXT", file=sys.stderr)
        return 1
    print(f"entry written: {len(TEXT)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
