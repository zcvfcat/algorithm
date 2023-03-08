import random


def insert(array):
    for idx in range(1, len(array)):
        while idx > 0 and array[idx - 1] > array[idx]:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1

    return array


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(insert(array))
