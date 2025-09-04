def quick(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quick(left) + middle + quick(right)

print(quick([3, 6, 8, 10, 1, 2, 1]))