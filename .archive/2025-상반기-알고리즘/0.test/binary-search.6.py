def binary_search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid + 1, end)
    else:
        return binary_search(array, start, mid - 1)
