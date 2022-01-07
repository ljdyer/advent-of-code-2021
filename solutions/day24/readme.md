# --- Day 24: Arithmetic Logic Unit ---

## Problem statement

[here](https://adventofcode.com/2021/day/24)

## Part One

Thank you to [JulienTT](https://www.reddit.com/user/JulienTT/) for [this post](https://www.reddit.com/r/adventofcode/comments/rnejv5/comment/hq57ov0/?utm_source=share&utm_medium=web2x&context=3) which helped me to understand that I could derive a system of equations for the values w1,w2,... by expressing value of z at each stage in base 26.

```
1	z = w1+6
2	z = w1+6 . w2+6
3	z = w1+6 . w2+6 . w3+3
4	z = w1+6 . w2+6 		        provided w4 = w3 - 8
5	z = w1+6 . w2+6 . w5+9
6	z = w1+6 . w2+6 		        provided w6 = w5 + 8
7	z = w1+6 . w2+6 . w7 + 13
8	z = w1+6 . w2+6 . w7+13 . w8+7
9	z = w1+6 . w2+6 . w7+13		    provided w9 = w8 + 6
10	z = w1+6 . w2+6 . w7+13 . w10+10
11	z = w1+6 . w2+6 . w7+13		    provided w11 = w10 + 5
12	z = w1+6 . w2+6			        provided w12 = w7 - 3
13	z = w1+6			            provided w13 = w2 - 1
14	z = 0				            provided w14 = w1 - 5
```

I will return later to tidy up the code and provide a longer explanation of the steps in my solution.