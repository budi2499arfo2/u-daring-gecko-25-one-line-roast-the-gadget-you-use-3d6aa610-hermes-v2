"""One-line roast: an app that demands five stars before it even opens.

The entry is a single line of at most 200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt by main(). The punch is the comparison:
a job interview — a formal process that vets you — asked less of me
than this app's loading screen.
"""

import os
import sys

TEXT = "This app asked for five stars before it even opened — my last job interview asked less of me than this loading screen."


def main() -> int:
    text = TEXT
    if not isinstance(text, str):
        print("entry is not text", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
