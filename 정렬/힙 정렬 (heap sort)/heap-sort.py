def heapify(unsorted, index, heap_size):
    largest = index

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    width = len(unsorted)

    for i in range(width//2 - 1, -1, -1):
        heapify(unsorted, i, width)

    for i in range(width - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)

    return unsorted


unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sortedArray = heap_sort(unsorted)

print(sortedArray)
