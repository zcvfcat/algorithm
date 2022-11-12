def merge_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted

    mid = len(unsorted) // 2
    low_array = merge_sort(unsorted[:mid])
    high_array = merge_sort(unsorted[mid:])

    merged_array = []

    low = 0
    high = 0

    while low < len(low_array) and high < len(high_array):
        if low_array[low] < high_array[high]:
            merged_array.append(low_array[low])
            low += 1
        else:
            merged_array.append(high_array[high])
            high += 1

    merged_array += low_array[low:]
    merged_array += high_array[high:]

    return merged_array
