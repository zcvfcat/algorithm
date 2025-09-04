def quick(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left, equal, right = [], [], []

    for v in range(len(arr)):
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)

    return quick(left) + equal + quick(right)
