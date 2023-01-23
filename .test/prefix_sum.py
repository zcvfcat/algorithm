array = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
]

prefix_sum = [[0 for _ in range(len(array[0]) + 1)] for _ in range(len(array) + 1)]

for y in range(len(array)):
    for x in range(len(array[0])):
        prefix_sum[y + 1][x + 1] = array[y][x] - prefix_sum[y - 1][x] - prefix_sum[y][x - 1] + prefix_sum[y][x]
