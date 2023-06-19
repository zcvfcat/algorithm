from collections import deque


def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left, right, merged = deque(merge(array[:mid])), deque(merge(array[mid:])), []

    while left and right:
        merged += [left.popleft()] if left[0] <= right[0] else [right.popleft()]

    merged += left + right

    return merged


# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(merge(arr1))

# Test Case 2
arr2 = []
expected_output2 = []
print(merge(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(merge(arr3))

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(merge(arr4))
