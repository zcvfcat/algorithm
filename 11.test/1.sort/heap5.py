def heap(array):
    length = len(array)

    for idx in range(length // 2 - 1, -1, -1):
        heapify(array, length, idx)

    for idx in range(length - 1, 0, -1):
        array[0], array[idx] = array[idx], array[0]
        heapify(array, idx, 0)


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
