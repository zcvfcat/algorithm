def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left, right, merged = merge(arr[:mid]), merge(arr[mid:]), []

    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return merged + left + right


def quick(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left, equal, right = [], [], []

    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)

    return quick(left) + equal + quick(right)


print(merge([3, 5, 1, 2, 3, 4, 5, 1, 2, 3, 45, 6, 7, 8, 3]))
print(quick([3, 5, 1, 2, 3, 4, 5, 1, 2, 3, 45, 6, 7, 8, 3]))
