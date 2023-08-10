def binarySearch(array, target, start, end):
    if start > end:
        return False  # None?

    mid = (start + end) // 2

    if array[mid] < target:
        return binarySearch(array, target, mid + 1, end)
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return mid

array = [0, 1, 3, 6, 7, 8, 9]
print(binarySearch(sorted(array), 8, 0, len(array)))
