def binary_search(array, target):
    start, end = 0, len(array) - 1
    array.sort()

    while start <= end:
        mid = (start + end) // 2
        value = array[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return mid

    return None
