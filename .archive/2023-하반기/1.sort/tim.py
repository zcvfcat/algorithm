def insert(arr, start, end):
    for node in range(start, end):
        idx = node

        while idx >= start and arr[idx] > arr[idx + 1]:
            arr[idx + 1], arr[idx] = arr[idx], arr[idx + 1]
            idx -= 1

    return arr


def merge(arr, start, mid, end):
    left, right, merged = arr[start:mid], arr[mid: end], []

    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return merged + left + right


def tim(arr, unit = 32):
    length = len(arr)

    for i in range(0, length, unit):
        arr = insert(arr, i, min(i + unit, length - 1))

    size = unit

    while size < length:
        for start in range(0, length, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, length)
            merged = merge(arr, start, mid, end)
            arr[start: start + len(merged)] = merged

        size *= 2
    
    return arr

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(tim(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(tim(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(tim(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(tim(arr4) == expected_output4)
