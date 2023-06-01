from collections import deque

def merge(array):
    if len(array) < 2:
        return array
    
    mid = len(array) // 2
    
    left, right = deque(merge(array[:mid])), deque(merge(array[mid:]))

    merged = []
    while left and right:
        if left[0] < right[0]:
            merge += [left.popleft()]
        elif right[0] < left[0]:
            merge += [right.popleft()]
    
    merged += left
    merged += right

    return merged


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

