# log2n
from functools import lru_cache

# lru_cache is a decorator
@lru_cache(maxsize=None)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number for n: "))
    print(f"The {n}th number in the Fibonacci sequence is {fib(n - 1)}")