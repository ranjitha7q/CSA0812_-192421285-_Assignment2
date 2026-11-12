"""Q7: Redesign Q6's repeated recursive work using an iterative solution.
The original naive recursion repeats the same subproblems. The redesigned
loop stores only the previous two values, giving O(n) time and O(1) space.
"""
import time

naive_calls = 0

def original_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return original_naive(n - 1) + original_naive(n - 2)

def redesigned_iterative(n):
    if n <= 1:
        return 1
    one_step_behind = 1
    two_steps_behind = 1
    for _ in range(2, n + 1):
        current = one_step_behind + two_steps_behind
        two_steps_behind = one_step_behind
        one_step_behind = current
    return one_step_behind

def timed(function, n):
    start = time.perf_counter()
    result = function(n)
    return result, time.perf_counter() - start

if __name__ == "__main__":
    for n in (10, 20, 25, 30):
        naive_calls = 0
        old_result, old_time = timed(original_naive, n)
        new_result, new_time = timed(redesigned_iterative, n)
        print(f"n={n}: same answer={old_result == new_result}")
        print(f"  original: calls={naive_calls:,}, time={old_time:.6f}s")
        print(f"  redesigned: loop iterations={max(0, n-1):,}, time={new_time:.6f}s")
    n = 1000
    result, elapsed = timed(redesigned_iterative, n)
    print(f"n={n}: iterative solution completed in {elapsed:.6f}s")
    print("Number of digits in answer:", len(str(result)))
