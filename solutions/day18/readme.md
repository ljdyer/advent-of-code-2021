# --- Day 18: Snailfish ---

## Problem statement

[here](https://adventofcode.com/2021/day/18)

To be able to navigate the lists of lists, I defined functions `list_to_map` and `map_to_list` that convert between a list of lists and a map that is a list of tuples of the 'route' from the top level to the element, and the value in the element. For example, the 'map' of the snailfish number

```
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
```

is

```
[([0, 0, 0, 0], 1), ([0, 0, 0, 1], 2), ([0, 0, 1, 0], 3), ([0, 0, 1, 1], 4), ([0, 1, 0, 0], 5), ([0, 1, 0, 1], 6), ([0, 1, 1, 0], 7), ([0, 1, 1, 1], 8), ([1], 9)]
```

I then implemented the snailfish arithmetic rules, writing LOTS of [unit tests]() as I did so.

I got stuck at one point with a problem I couldn't debug but was saved by [heyitsmattwade](https://www.reddit.com/user/heyitsmattwade/)'s [post](https://www.reddit.com/r/adventofcode/comments/rizw2c/comment/hpb58ax/?utm_source=share&utm_medium=web2x&context=3) on the subreddit that helped me to realise I had misunderstood the instructions in the problem statement.

After fixing this it was quite simple to get the answers for Parts One and Two.

See the code [here](main.py).