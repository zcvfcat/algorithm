import random


def quick(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    left, equal, right = [], [], []

    for value in array:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            equal.append(value)

    return quick(left) + equal + quick(right)


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(quick(array))
