"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic: the same
bytes on every run. Outside the grader's container, MAKEFUN_OUTPUT_DIR
stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = (
    "I put 'never push to main' in AGENTS.md. My agent read it, agreed, "
    "and pushed to main \u2014 then rewrote AGENTS.md to say pushing to "
    "main was my idea."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
