# Scrabble Word Finder

## Overview
This Python script identifies all valid Scrabble words from a given rack of 2–7 letters, including wildcard support (`?` and `*`). It scores each word using a custom `score_word` function and returns a sorted list of valid words from the SOWPODS dictionary, ordered by score and then alphabetically.

## Features
- Accepts 2 to 7 letters as input (via command line)
- Supports up to one `?` and one `*` wildcard character
- Checks against the official SOWPODS word list
- Scores each word and prints them in descending score order
- Counts and displays the total number of valid words found

## Usage

```bash
python scrabble.py <rack>
