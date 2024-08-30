def quick(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    left, equal, right = [], [], []

    for v in array:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)

    return quick(left) + equal + quick(right)