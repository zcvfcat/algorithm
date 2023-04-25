def insert_sort(array: list, start, end):
    for node in range(start, end):
        idx = node

        while idx >= start and array[idx] > array[idx + 1]:
            array[idx + 1], array[idx] = array[idx], array[idx + 1]
            idx -= 1

    return array


def merge(array, start, mid, end):
    left = array[start: mid]
    right = array[mid: end]

    sorted_array = []

    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    sorted_array += left
    sorted_array += right

    return sorted_array


def tim_sort(array, unit=32):
    length = len(array)
    for i in range(0, length, unit):
        array = insert_sort(array, i, min(i + unit, length))

    size = unit

    while size < length:
        for start in range(0, length, size * 2):
            mid = start + size - 1
            end = min(start + size * 2 - 1, length)
            merged_array = merge(array, start, mid, end)
            array[start: start + len(merged_array)] = merged_array

        size *= 2

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
