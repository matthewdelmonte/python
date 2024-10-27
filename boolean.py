# log2n

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter a number for n: "))
print(f"The {n}th number in the fibonaci sequence is {fib(n)}")

if __name__ == "__main__":
    fib(n)