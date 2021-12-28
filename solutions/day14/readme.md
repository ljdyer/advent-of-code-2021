# --- Day 14: Extended Polymerization ---

## Problem statement

[here](https://adventofcode.com/2021/day/14).

## Part One

Solved using the naive method of generating the full string for each step.

See the code [here](solution-part-one.py).

## Part Two

Solved with help from [Bradley Sward's video](https://www.youtube.com/watch?v=4d2gEYShtVA).

Overcame memory issues from storing strings at each step by counting the number of times each pair appears at each step using a dictionary.

Calculated final letter frequencies based on the observation that the actual frequency of each letter adjusted for overlapping letters is the ceiling of the number obtained from the dictionary of pair frequencies (though I stil don't fully understand why this is the case).

See the code [here](solution-part-two.py).