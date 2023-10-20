import random


def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right, merged = merge(arr[:mid]), merge(arr[mid:]), []

    while left and right:
        merged.append(left.pop(0) if left[0] < right[0] else right.pop(0))

    return [*merged, *left, *right]


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(merge(array))
