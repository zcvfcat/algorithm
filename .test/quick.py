def quick(array):
    if len(array) < 2:
        return array

    pivot = array[len(array)//2]
    left, equal, right = [], [], []

    for i in array:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)

    return quick(left) + equal + quick(right)


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(quick(arr))
