from collections import deque


def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left, right = deque(merge(arr[:mid])), deque(merge(arr[mid:]))

    sorted_array = []

    while left and right:
        if left[0] < right[0]:
            sorted.append(left.popleft())
        elif right[0] <= right[0]:
            sorted_array.append(right.popleft())

    sorted_array.extend(left)
    sorted_array.extend(right)

    return sorted_array
