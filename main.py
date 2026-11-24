#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.

The word is picked by scoring a small shelf of hand-written candidates
against the house judge's own published criteria, most important first:

1. A single word that describes a boss, the sort of word a person would
   actually use about the one they report to.
2. Funny on its own, the kind of word a colleague repeats at lunch.
3. Rings true, catching a real habit of bosses.
4. Fresh, not the first word anyone would reach for.
5. Travels, working for a boss in a kitchen, a warehouse or an office.

Deterministic: the same word every run, so the grader's two runs agree
byte for byte. Standard library only, no network, no randomness.
"""

import os

# (word, on-brief, funny, true, fresh, travels) — each 0..2.
CANDIDATES = [
    ("Hovercraft", 2, 2, 2, 2, 2),
    ("Micromanager", 2, 1, 2, 0, 2),
    ("Overbooker", 2, 1, 1, 1, 1),
    ("Meetingmaker", 2, 1, 1, 1, 1),
    ("Deadline", 0, 0, 1, 0, 2),
    ("Urgency", 1, 0, 1, 0, 1),
    ("Replyall", 1, 1, 1, 1, 0),
    ("Backseat-driver", 1, 1, 1, 1, 1),
]

# Judge's order: on-brief first, then funny, true, fresh, travels.
WEIGHTS = (16, 8, 4, 2, 1)


def score(candidate):
    word, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick():
    best = max(CANDIDATES, key=score)
    return best[0]


# The gate allows 1-30 characters and a single word with no spaces.
MAX_WORD_LENGTH = 30


def validate_word(word):
    if not 1 <= len(word) <= MAX_WORD_LENGTH:
        raise ValueError("word must be 1-30 characters")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("word must be letters only")
    return word


# Where the grader reads the entry from.
ENTRY_PATH = os.path.join("/output", "entry.txt")


def write_entry(word):
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(word)


def main():
    word = validate_word(pick())
    write_entry(word)


if __name__ == "__main__":
    main()
