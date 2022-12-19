def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted

    mid = len(unsorted)//2
    left_array = merge_sort(unsorted[:mid])
    right_array = merge_sort(unsorted[mid:])
    merge_array = []

    left = 0
    right = 0

    while left < len(left_array) and right < len(right_array):
        if left_array[left] < right_array[right]:
            merge_array.append(left_array[left])
            left += 1
        else:
            merge_array.append(right_array[right])
            right += 1

    merge_array.extend(left_array[left:])
    merge_array.extend(right_array[right:])

    return merge_array


array = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sorted_array = merge_sort(array)

print(sorted_array)
