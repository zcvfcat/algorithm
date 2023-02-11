def quick(array: list) -> list:
    if len(array) < 2:
        return array

    pivot = array[len(array)//2]

    left, equal, right = [], [], []

    for value in array:
        if value < pivot:
            left += [value]
        elif value > pivot:
            right += [value]
        else:
            equal += [value]

    return quick(left) + equal + quick(right)


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(quick(arr))
