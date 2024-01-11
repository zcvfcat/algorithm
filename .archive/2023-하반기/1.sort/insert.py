import random


def insert(arr):
    for start in range(len(arr)):
        while start > 0 and arr[start] < arr[start - 1]:
            arr[start], arr[start - 1] = arr[start - 1], arr[start]
            start -= 1

    return arr


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(insert(array))
