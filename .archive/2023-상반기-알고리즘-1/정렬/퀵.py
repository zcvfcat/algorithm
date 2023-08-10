def quick(array) -> list:
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]

    left, equal, right = [], [], []

    for node in array:
        if node < pivot:
            left.append(node)
        elif node == pivot:
            equal.append(node)
        else:
            right.append(node)

    return quick(left) + equal + quick(right)


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(quick(arr))
