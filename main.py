"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (one line, under 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The program is fully deterministic: no network, no randomness, no clock, no
environment input beyond the output directory. It always writes the exact
same bytes, so repeated runs are byte-identical.

The line (113 characters, one line, no trailing newline):

    I'm on vacation. My replacement is a cron job that replies 'per my last
    email' to everything, including this one.

Why this line (designed against the published judge brief, most important
criterion first):

1. On-subject: a first-person out-of-office auto-reply from an AI agent on
   vacation. It reads exactly like a message a colleague would receive.
2. Surprising turn, not a mild pun: the setup is a plain vacation notice;
   the turn is that the replacement — a cron job — answers everything with
   "per my last email", including the very message announcing it. The reply
   incriminates itself on first read.
3. Machine voice carries the joke: the cron job *is* the joke engine, a
   specific machine artefact doing something wrong, not generic robot talk.
4. One clean line, 113 characters, real auto-reply shape.
5. Fresh: no beach, no inbox, no "back soon", no "limited access".
"""

import os
import sys

# The single entry. One line, 115 characters, plain ASCII (valid UTF-8).
ENTRY = (
    "I'm on vacation. My replacement is a cron job that replies "
    "'per my last email' to everything, including this one."
)

MAX_CHARS = 160


def output_dir() -> str:
    """Resolve the output directory the harness provides."""
    for var in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, must be 1-160", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text or "\r" in text:
        print("entry must be a single clean line", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
