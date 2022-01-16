# --- Day 16: Packet Decoder ---

## Problem statement

[here](https://adventofcode.com/2021/day/16)

## Part One

I had a [longer, more complicated solution](solution-part-one-old.py) that passed the tests but either got stuck somewhere or was taking too long on my actual puzzle data. Then realised that I could make it much simpler by focusing only on the version numbers and discarding literal values, lengths/numbers of sub-packets, etc. thanks to [kruvik](https://www.reddit.com/user/kruvik/)'s [code](https://www.reddit.com/user/kruvik/) posted in the subreddit. My solution uses a global variable `version_num_counter` to count version numbers—I would like to refactor in the future to remove the dependence on global variables.

See the code [here](solutions/solution-part-one.py).

## Part Two

I was able to solve this myself, although my solution is dependent on global variables and feels a little bit scrappy so I'd like to take a look at some alternative solutions and clean it up a bit in the future.

I use the same basic parsing logic as before, but store each packet's `type_id`, along with other information required for tracking the packet heirachy, in a nested dictionary where the keys of the top dictionary are unique integer IDs for each packet:

```
0 : {'type_id': 0, 'length': 5327, 'parent': None, 'operator_type': 'len', 'required': 5305}
1 : {'type_id': 2, 'length': 166, 'parent': 0, 'operator_type': 'len', 'required': 144}
2 : {'type_id': 4, 'value': 784, 'length': 21, 'parent': 1}
3 : {'type_id': 4, 'value': 30800350288, 'length': 51, 'parent': 1}
4 : {'type_id': 4, 'value': 45345613, 'length': 41, 'parent': 1}
etc...
```

I track the packets that are currently 'open' (incomplete) in a list of IDs from which I pop the last value when the length/sub-packet number requirement for the last open packet is satisfied.

I apply the evaluation rules at the end in the `evaluate_packet` function.

I ran into an issue with numpy integer overflow at the end which was causing the answer to come out as 18217636600268 rather than 18234816469452. Importing `math.prod` instead of `numpy.prod` solved it. I had run into this issue on a previous AOC problem so I should have known better than to use `numpy.prod`.

See the code [here](solution-part-two.py).