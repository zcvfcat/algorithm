def shell_sort(unsorted):
    width = len(unsorted)
    gap = width // 2  # 구간

    while gap > 0:
        for index in range(gap, width):
            temp = unsorted[index]
            j = index

            while j >= gap and unsorted[j-gap] > temp:
                unsorted[j] = unsorted[j-gap]
                j -= gap
            unsorted[j] = temp
        gap //= 2


unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sortedArray = shell_sort(unsorted)

print(sortedArray)
