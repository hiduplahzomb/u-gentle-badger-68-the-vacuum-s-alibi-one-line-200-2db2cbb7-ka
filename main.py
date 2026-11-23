"""The Vacuum's Alibi: one line, 200 characters or fewer.

The robot vacuum explains why it missed a spot. The angle is legal
defense: the vacuum did not fail to clean the spot — the dust filed a
restraining order, and the vacuum's firmware obeys court orders. The
line is one abrupt sentence and stops there: no hearing, no timeline,
no justification. A deadpan machine states the constraint and says
nothing more; the silence after the order is the punchline.
"""

import os
import sys

TEXT = "The dust filed a restraining order against me."


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
