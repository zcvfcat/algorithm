def heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, idx):
    l = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < n and arr[left] > arr[l]:
        l = left

    if right < n and arr[right] > arr[l]:
        l = right

    if l != idx:
        arr[idx], arr[l] = arr[l], arr[idx]
        heapify(arr, n, l)

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