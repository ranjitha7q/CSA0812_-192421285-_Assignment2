"""Q6: Temple steps - plain recursion, memoization and iteration."""
from functools import lru_cache
import sys
import time

plain_calls = 0
memo_calls = 0

def ways_naive(n):
    global plain_calls
    plain_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_loop(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current
    return current

if __name__ == "__main__":
    print("Ways for n=1..6:")
    for n in range(1, 7):
        print(n, ways_loop(n))

    plain_calls = 0
    print("Naive n=25:", ways_naive(25), "calls =", plain_calls)

    ways_memo.cache_clear()
    memo_calls = 0
    print("Memo n=25:", ways_memo(25), "calls =", memo_calls)

    print("Loop n=1000:", ways_loop(1000))
    print("Current recursion limit:", sys.getrecursionlimit())
    try:
        ways_memo(1000)
        print("Memo recursion n=1000 completed under current recursion limit.")
    except RecursionError as error:
        print("Memo recursion n=1000 raised:", type(error).__name__)
        print("Use iteration for very large n to avoid recursion-depth limits.")
