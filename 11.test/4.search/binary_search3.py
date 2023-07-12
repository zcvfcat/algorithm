def binary_search(array: list, target: int):
    array.sort()

    start, end = 0, len(array)
    while start < end:
        mid = (start + end) // 2
        value = array[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return mid

    return None
