# Uses memoization to memorize bases cases
# Results in saving time, computation and unnecessary recursion depth.

from typing import Dict

memo: Dict[int, int] = {0:0, 1:1}

def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-2) + fib(n-1)
    return memo[n]


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    print(fib(n))
