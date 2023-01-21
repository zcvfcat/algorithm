def merge(array) -> list:
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_array = merge(array[:mid])
    right_array = merge(array[mid:])

    merge_array = []

    while left_array and right_array:
        if left_array[0] < right_array[0]:
            merge_array.append(left_array.pop(0))
        else:
            merge_array.append(right_array.pop(0))

    merge_array += left_array
    merge_array += right_array

    return merge_array


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(merge(arr))
