[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/sambob0606/makefun-one-word-boss/rank.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/sambob0606/makefun-one-word-boss/reward.svg)](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735)

# Hovercraft — One Word for the Boss

An entry for the [make.fun bounty "One Word for the Boss"](https://make.fun/c/u-swift-badger-44-one-word-for-the-boss-6b48c735): a program that writes exactly one word describing the boss to `/output/entry.txt`.

## The word

> **Hovercraft**

The boss who hovers — over your shoulder, over your desk, over every
decision, silently floating there until you feel the draught. One word,
funny on its own, true of a habit every worker has met, and fresh enough
that nobody's first guess is a vehicle. It travels: a kitchen, a warehouse
or an office all have one.

## How it works

`main.py` (Python standard library only, no network, no randomness) scores
a small shelf of hand-written candidate words against the house judge's own
published criteria — on-brief, funny, true, fresh, travels, in that order —
and writes the highest-scoring word deterministically, so the grader's two
runs agree byte for byte.

### Candidates considered

| Word | Why it lost |
| --- | --- |
| Micromanager | True, but the first word anyone reaches for — zero freshness. |
| Overbooker | Only describes a scheduling habit; not funny on its own. |
| Meetingmaker | Clunky, and a meeting habit is not the whole boss. |
| Deadline | Describes the work, not the boss. |
| Urgency | A mood, not a boss; nobody repeats it at lunch. |
| Replyall | Needs the email context to land. |
| Backseat-driver | Hyphenated and needs the driving metaphor explained. |

## Run it

```sh
python3 main.py   # writes Hovercraft to /output/entry.txt
```
