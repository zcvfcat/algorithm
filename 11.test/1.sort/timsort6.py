from collections import deque

def insert_sort(array, start, end):
    for idx in range(start, end):
        while idx > start and array[idx] < array[idx - 1]:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1
    return array

def merge(array, start, mid, end):
    left, right, merged = deque(array[start: mid]), deque(array[mid: end]), []

    while left and right:
        merged += [left.popleft()] if left[0] < right[0] else [right.popleft()]

    return merged + left + right



def tim_sort(array, unit = 32):
    # 단위 쪼개기
    for start in range(0, len(array), unit):
        array = insert_sort(array, start, min(start + unit, len(array)))
    
    while unit < len(array):
        for start in range(0, len(array), unit * 2):
            mid = start + unit - 1
            end = min(start + unit * 2 - 1, len(array))
            merged = merge(array, start, mid, end)

            array[start: start + len(merged)] = merged
        
        unit *= 2

    return array

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(tim_sort(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(tim_sort(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(tim_sort(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(tim_sort(arr4) == expected_output4)
