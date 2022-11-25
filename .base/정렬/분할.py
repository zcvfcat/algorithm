def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_array = merge(array[:mid])
    right_array = merge(array[mid:])
    merge_array = []

    left = 0
    right = 0

    while left < len(left_array) and right < len(right_array):

        if left_array[left] < right_array[right]:
            merge_array.append(left_array[left])
            left+=1
        else:
            merge_array.append(right_array[right])
            right+=1

    merge_array.extend(left_array[left:])
    merge_array.extend(right_array[right:])

    return merge_array

array = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sorted_array = merge(array)

print(sorted_array)