unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(unsorted)

for i in range(width - 1, 0, -1):
    for j in range(i):
        if unsorted[j] > unsorted[j + 1]:
            unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

print(unsorted)
