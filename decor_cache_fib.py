# Uses the built-in Python decorater which caches the value
# This works same as memo_fib.py, just that Python does the memoization for us.

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == "__main__":
    n = int(input("Enter a number"))
    print(fib(n))
