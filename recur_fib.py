# Fibonacci 

# Calculating fibonacci using recursion
# Every non-base case call results in 2 more calls.
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fib(n))

    
