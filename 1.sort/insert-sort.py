import random


def insert(array):
    for limit in range(1, len(array)):

        for idx in range(limit, 0, -1):
            if array[idx - 1] > array[idx]:
                array[idx - 1], array[idx] = array[idx], array[idx - 1]

    return array


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(insert(array))
