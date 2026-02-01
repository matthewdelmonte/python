# Fibonacci sequence find the number in the sequence for n
# Find the solution to the Fibonacci sequence for n in my journal

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("Enter a number for n: "))
print(f"The {n}th number in the fibonacci sequence is {fibo(n)}")

if __name__ == "__main__":
    fibo(n)