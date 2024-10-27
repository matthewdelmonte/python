# Fibonaci Sequence Find the number in the sequence for n

def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

n = int(input("Enter a number for n: "))
print(f"The {n}th number in the fibonaci sequence is {fibonaci(n)}")

if __name__ == "__main__":
    fibonaci(n)