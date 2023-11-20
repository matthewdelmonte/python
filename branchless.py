import time

st = time.process_time()
def smaller_branchless(a: int, b: int):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Invalid argument type. Both arguments must be integers.")

    return a * (a < b) + b * (b <= a)

et = time.process_time()
elapsed_time = (st - et) * 1000
print(f'The function took {elapsed_time:.4f} milliseconds to run.')
print(smaller_branchless(820, 350))