nums = [15, 8, 2, 10, 12, 45, 23, 9]

def binary_search(array, target):
    left = 0
    right = len(array) -1

    while (left <= right):
        mid = (right + left) // 2

        if array[mid] == target:
            return f"The target number is: {nums[mid]}!"
        elif array[mid] < target:
            left = mid +1
        else:
            right = mid -1

    return f"The target number was not found in the array."

print(binary_search(nums, 12))