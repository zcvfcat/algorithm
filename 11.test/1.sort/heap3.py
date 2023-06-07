def heap(array):
    length = len(array)

    for idx in range(length // 2 - 1, -1, -1):
        heapify(array, length, idx)

    for idx in range(length - 1, 0, -1):
        array[0], array[idx] = array[idx], array[0]
        heapify(array, idx, 0)
    
    return array


def heapify(array, n, idx):
    current = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and array[left] > array[current]:
        current = left

    if right < n and array[right] > array[current]:
        current = right

    if current != idx:
        array[idx], array[current] = array[current], array[idx]
        heapify(array, current, idx)

# Test Case 1
arr1 = [3, 2, 1]
expected_output1 = [1, 2, 3]
print(heap(arr1) == expected_output1)

# Test Case 2
arr2 = []
expected_output2 = []
print(heap(arr2) == expected_output2)

# Test Case 3
arr3 = [1, 1, 1]
expected_output3 = [1, 1, 1]
print(heap(arr3) == expected_output3)

# Test Case 4
arr4 = [5, 1, 7, 9, 2, 10]
expected_output4 = [1, 2, 5, 7, 9, 10]
print(heap(arr4) == expected_output4)