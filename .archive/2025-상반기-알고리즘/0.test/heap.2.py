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


def heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr
