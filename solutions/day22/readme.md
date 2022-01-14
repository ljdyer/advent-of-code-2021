# --- Day 22: Reactor Reboot ---

## Problem statement

[here](https://adventofcode.com/2021/day/22)

## Part One

Brute force solution modelling reactor core as a 3D matrix (list of lists of lists) with boolean values representing on or off states and toggling individual cubes on or off as per instructions.

See the code [here](solutions/solution-part-one.py).

## Part Two

Brute force solution takes too long, so dealt only in whole cuboids (tracking start and end positions for x, y, and z rather than toggling individual cubes on/off).

Defined a class `Cuboid` and a function `difference` to return a list of cuboids that cover all the cubes that are included in one cuboid but not in another.

Took some inspiration from the [subreddit](https://www.reddit.com/r/adventofcode/comments/rlxhmg/2021_day_22_solutions/) and in particular [this paste](https://pastebin.com/vKSar4KB) (apologies, I can't locate the original post now).

My solution still takes over an hour to complete but I decided to suck it up and wait it out this time and will come back later to try to work out where it can be optimised.

See the code [here](solutions/solution-part-two.py).
