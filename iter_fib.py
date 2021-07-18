# Solves fibonacci iteratively

def fib(n: int) -> int:
    if n == 0 : return n
    last: int = 0 # last num
    next: int = 1 # next num

    for _ in range(1, n):
        temp = last
        last = next
        next = temp + next
    return next


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fib(n))
