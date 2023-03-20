def quick(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    left, equal, right = [], [], []

    for value in arr:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            equal.append(value)

    return quick(left) + equal + quick(right)
