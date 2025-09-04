def heap_sort(arr):
    n = len(arr)

    def heapify(index, heap_size):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < heap_size and arr[left] > arr[largest]:
            largest = left
        if right < heap_size and arr[right] > arr[largest]:
            largest = right

        if largest != index:
            arr[index], arr[largest] = arr[largest], arr[index]
            heapify(largest, heap_size)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(i, n)

    # Extract elements one by one
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(0, end)

    return arr


