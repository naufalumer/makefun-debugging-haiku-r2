"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to entry.txt in the output directory.
The haiku is three lines in the 5-7-5 syllable shape, seventeen syllables
in total. Standard library only.
"""

import os

HAIKU_LINES = [
    "midnight, one red line",
    "the logs all swear nothing changed",
    "git blame says my name",
]

HAIKU = "\n".join(HAIKU_LINES) + "\n"


def main():
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Refuse to write anything that would fail it.
    text = HAIKU
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit("haiku fails the 1-200 character gate")
    if len(HAIKU_LINES) != 3:
        raise SystemExit("haiku must be exactly three lines")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
