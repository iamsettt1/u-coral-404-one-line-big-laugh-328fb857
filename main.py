#!/usr/bin/env python3
"""One Line, Big Laugh — a single original funny line.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output)
and prints exactly that line, nothing else. Deterministic: the same
line on every run. Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = 'My resume says I\'m a team player, which is corporate for "I have cried in three different office bathrooms."'


def main() -> None:
    # The sealed scorer only accepts 1-200 characters; never emit more.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
