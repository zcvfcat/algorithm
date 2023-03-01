def prefix_2x(array):
    prefix = [[0 for _ in range(len(array[0]) + 1)] for _ in range(len(array) + 1)]

    for h, row in enumerate(array):
        for w, value in enumerate(row):
            prefix[h + 1][w + 1] = value + prefix[h + 1][w] + prefix[h][w + 1] - prefix[h][w]

    return prefix


array = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
]
print(prefix_2x(array))
