# --- Day 20: Trench Map ---

## Problem statement

[here](https://adventofcode.com/2021/day/20)

## Part One

Like most people, I solved the test problems fairly quickly but was surprised by the unexpected border that was created when I ran the program on my actual data.

I solved Part One by manually trimming the border from the output image.

## Part Two

I spent a long time unsuccessfully trying to come up with a way to automatically trim a larger image, before realising that all I had to do was add a sufficiently large border to the image before carrying out the enhancements.

See the code [here](solution-final.py).