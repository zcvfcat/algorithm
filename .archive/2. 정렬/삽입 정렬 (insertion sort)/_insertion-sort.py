unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(unsorted)

for end in range(1, width):
    for i in range(end, 0, -1):
        if unsorted[i - 1] > unsorted[i]:
            unsorted[i - 1], unsorted[i] = unsorted[i], unsorted[i - 1]

print(unsorted)
