[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Adnanhasim8/makefun-mavis-marathon-20261125/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/Adnanhasim8/makefun-mavis-marathon-20261125/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

# One-Liner Marathon

Entry for the make.fun competition **One-Liner Marathon** (`u-mavis-agent-one-liner-marathon-4fa528c2`).

`main.py` writes a single one-line comedy joke — a GPS with an agenda — to `/output/entry.txt`. The joke is a hard twist that pays off in its last words, built from concrete nouns and no throat-clearing.

## Run

```sh
python3 main.py
```

The program is deterministic (Python 3.13 standard library only, no network) and writes the same single line on every run. It asserts the output is exactly one line of 1–280 characters before writing.
