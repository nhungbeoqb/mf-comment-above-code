#!/usr/bin/env python3
"""Write the entry line for 'The Comment Above the Code' to entry.txt.

The line is a single comment a developer might have left above fragile
production code: funny because it is true, with the punch landing at the
end. Output goes to the directory named by MAKEFUN_OUTPUT_DIR, defaulting
to /output (the grader's sandbox), so the program is deterministic and
needs no network, no input files and no secrets.
"""

import os

LINE = "// This is wrong in exactly the way the tax office expects. Fix it and we owe \u00a340,000."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
