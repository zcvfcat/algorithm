def insert(arr):
    for i in range(len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def merge(arr, unit):
    if len(arr) < unit:
        return arr

    mid = len(arr) // 2
    left, right, merged = merge(arr[:mid]), merge(arr[mid:]), []

    while left and right:
        merged += left.pop(0) if left[0] < right[0] else right.pop(0)

    return merged + left + right


def timsort(arr, unit=8):
    for i in range(0, len(arr), unit):
        arr = insert(arr, i, min(i + unit, len(arr)))

    return merge(arr, unit)
