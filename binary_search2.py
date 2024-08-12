# Binary Search modules are part of the Python Standard Library

"""
import bisect as bi

def main():
    list = [1, 2, 3, 4, 5 ]
    
    x = 6
    
    i = bi.bisect_left(list, x)
    
    print(list, i)
    
    list.insert(i, x)
    
    print(list)

    Python documentation: https://docs.python.org/3/library/bisect.html

"""
    
def bisect(arr: list, x) -> int:
    lo = 0
    hi = len(arr)
    print(f"hi: {hi}")

    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid

    return lo

if __name__ == '__name':
    bisect()