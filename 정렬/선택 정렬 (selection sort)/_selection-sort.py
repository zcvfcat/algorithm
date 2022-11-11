unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(unsorted)

for i in range(width - 1):
    midx = i
    for j in range(i + 1, width):
        if unsorted[j] < unsorted[midx]:
            midx = j

    unsorted[i], unsorted[midx] = unsorted[midx], unsorted[i]

print(unsorted)
