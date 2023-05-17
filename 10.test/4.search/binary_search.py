def recur_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recur_search(array, target, start, mid - 1)
    else:
        return recur_search(array, target, mid + 1, end)

array = [0, 1, 3, 6, 7, 8, 9]
print(recur_search(sorted(array), 8, 0, len(array)))
