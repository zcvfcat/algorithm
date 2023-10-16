def insert(arr, start, end):
    for i in range(start, end):
        while start <= i and arr[i + 1] < arr[i]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]
            i -= 1

    return arr


def merge(arr, start, mid, end):
    left, right, merged = arr[:mid], arr[mid:], []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)

    return merged


def tim(arr):
    l = len(arr)
    unit = 32

    for i in range(0, l, unit):
        arr = insert(arr, i, min(i + unit, l - 1))

    size = unit

    while size < l:
        for start in range(0, l, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, l)
            merged = merge(arr, start ,mid, end)
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
