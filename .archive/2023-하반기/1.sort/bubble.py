import random


def bubble(arr):
    for end in range(len(arr) - 1, -1, -1):
        for idx in range(end):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(bubble(array))
