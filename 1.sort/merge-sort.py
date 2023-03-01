from collections import deque
import random


def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left, right = deque(merge(array[:mid])), deque(merge(array[mid:]))

    sorted_array = []

    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.popleft())
        elif right[0] <= right[0]:
            sorted_array.append(right.popleft())

    sorted_array.extend(left)
    sorted_array.extend(right)

    return sorted_array


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(merge(array))
