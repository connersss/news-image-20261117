#!/usr/bin/env python3
"""news-image-20261117: one image summing up Tuesday 17 November 2026.

The image (news.jpg, a 1024x1024 JPEG) is a front page: a masthead naming
the date, four panels for the day's biggest stories, and a footer strip
with four more. This program copies it to /output/entry.png, byte for
byte. No network, no randomness: two runs write identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.jpg"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT = OUTPUT_DIR / "entry.png"
MAX_BYTES = 1_048_576  # the gate: a whole PNG or JPEG of at most 1 MiB


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    size = SOURCE.stat().st_size
    if size > MAX_BYTES:
        print(f"image too large: {size} bytes > {MAX_BYTES}", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
