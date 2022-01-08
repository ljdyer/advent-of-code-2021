# --- Day 24: Arithmetic Logic Unit ---

## Problem statement

[here](https://adventofcode.com/2021/day/24)

## Part One

I started by writing the [translate_all.py](solution/translate_all.py) module to 'translate' the sample and actual MONADs into Python and simplify where possible using regular expressions. E.g.:

```
inp z       ==>     z = int(input_.pop(0))
inp x       ==>     x = int(input_.pop(0))
mul z 3     ==>     z = z * 3
eql z x     ==>     z = int(z==x)
```

I then put the test MONADs into functions and ran the tests in [test.py](tests/test.py) to confirm that the translation was correct.

I was now able to get the result of the MONAD for any input, but found that I needed a more efficient solution than the brute-force approach of trying every number from 99999999999999 until I found a solution.

I went through simplifying the translated version of MONAD_V1 by hand in the code editor (in [main.py](solution/main.py)) to get MONAD_V2, testing that the two versions gave the same outputs for random inputs at various stages as I did so, and found that I was able to eliminate the helper variables `x` and `y`:

```python
# ====================
def MONAD_v2(i):

    z = 0
    i = list(map(int, list(i)))

    # Step 1
    z = z * 26 + i[0] + 6

    # Step 2
    z = z * 26 + i[1] + 6

    # Step 3
    z = z * 26 + i[2] + 3

    # Step 4
    if i[3] == z % 26 - 11:
        z = z // 26
    else:
        z = (z // 26) * 26 + i[3] + 11

    ...
```

I got stuck with what to do next so consulted the subreddit. Thank you to [JulienTT](https://www.reddit.com/user/JulienTT/) for [this post](https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hq57ov0/?utm_source=share&utm_medium=web2x&context=3) which helped me to understand that I could derive a system of equations for the values w1,w2,... by considering the base 26 representation of `z` after each step

```
1	z = w1+6
2	z = w1+6 . w2+6
3	z = w1+6 . w2+6 . w3+3
4	z = w1+6 . w2+6				provided w4 = w3 - 8
5	z = w1+6 . w2+6 . w5+9
6	z = w1+6 . w2+6				provided w6 = w5 + 8
7	z = w1+6 . w2+6 . w7 + 13
8	z = w1+6 . w2+6 . w7+13 . w8+7
9	z = w1+6 . w2+6 . w7+13			provided w9 = w8 + 6
10	z = w1+6 . w2+6 . w7+13 . w10+10
11	z = w1+6 . w2+6 . w7+13			provided w11 = w10 + 5
12	z = w1+6 . w2+6				provided w12 = w7 - 3
13	z = w1+6				provided w13 = w2 - 1
14	z = 0					provided w14 = w1 - 5
```

From here I was able to derive the maximum and minimum solutions in my head.