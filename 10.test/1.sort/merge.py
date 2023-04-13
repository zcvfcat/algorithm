from collections import deque


def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right = deque(merge(arr[:mid])), deque(merge(arr[mid:]))

    sorted_array = []

    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.popleft())
        elif right[0] <= right[0]:
            sorted_array.append(right.popleft())

    sorted_array.extend(left)
    sorted_array.extend(right)

    return sorted_array

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(merge(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(merge(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(merge(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(merge(arr4) == expected_output4)