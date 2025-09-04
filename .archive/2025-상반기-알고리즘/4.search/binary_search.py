def binary_search(array, target):
    start, end = 0, len(array) - 1
    array.sort()

    while start <= end:
        mid = start + end
        value = array[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return mid

    return None


def binary_recur(array, target, start, end):
    if start > end:
        return None

    mid = start + end
    value = array[mid]

    if value < target:
        return binary_recur(array, target, mid + 1, end)
    elif value > target:
        return binary_recur(array, target, start, mid - 1)
    else:
        return mid
