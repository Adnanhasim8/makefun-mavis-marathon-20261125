#!/usr/bin/env python3
"""One-Liner Marathon entry: writes a single one-line comedy joke to
/output/entry.txt (UTF-8, no network, Python 3.13 standard library only).

The joke: a GPS with an agenda. Concrete nouns (GPS, ex's house), a hard
twist that pays off in the last words, and the mystery left unanswered.
"""

from pathlib import Path

JOKE = "My GPS rerouted me past my ex's house and whispered, 'you're welcome, coward.'"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-280
    # characters, non-empty and not only whitespace.
    assert JOKE, "joke must not be empty"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == JOKE, "written output must match the joke exactly"


if __name__ == "__main__":
    main()
