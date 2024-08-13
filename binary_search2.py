# Binary Search modules are part of the Python Standard Library
# Python documentation: https://docs.python.org/3/library/bisect.html

#"""
import bisect as bi
from functools import cache

@cache
def main():
    myList = list(range(0, 100000, 2))
    
    x = 100002
    i = bi.bisect_left(myList, x)
    #print(myList, i)
    
    myList.insert(i, x)
    print(myList[i])

if __name__ == '__main__':
    main()
#"""
    
# # bisect_left() function
# def bisect(arr: list, x) -> int:
#     lo = 0
#     hi = len(arr)
#     print(f"array length: {hi}")

#     while lo < hi:
#         mid = (lo + hi) // 2
#         if arr[mid] < x:
#             lo = mid + 1
#         else:
#             hi = mid

#     return lo

# if __name__ == '__name':
#     bisect()