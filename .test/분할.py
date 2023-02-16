def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left
    result += right

    return result


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(merge(arr))
