"""Q4: Compare repeated +=, list + join(), and f-string line creation."""
import time
import statistics

def build_plus(parts):
    text = ""
    for part in parts:
        text += part
    return text

def build_join(parts):
    return "".join(parts)

def build_fstrings(items):
    parts = [f"SMS {i}: Rs. {i % 50}" for i in items]
    return "".join(parts)

def average_time(function, argument, repeats=3):
    samples = []
    result = None
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(argument)
        samples.append(time.perf_counter() - start)
    return statistics.mean(samples), result

if __name__ == "__main__":
    for count in (1_000, 10_000, 200_000):
        parts = [f"SMS {i}: Rs. {i % 50}\\n" for i in range(count)]
        items = range(count)
        plus_time, plus_result = average_time(build_plus, parts)
        join_time, join_result = average_time(build_join, parts)
        f_time, f_result = average_time(build_fstrings, items)
        print(f"Lines: {count:,}")
        print(f"  += average:       {plus_time:.6f} s")
        print(f"  join average:     {join_time:.6f} s")
        print(f"  f-string average: {f_time:.6f} s")
        print(f"  outputs equal: {plus_result == join_result == f_result}")
