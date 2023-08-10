"""
구간합
"""

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# prefix_sum = [0]
# for i in range(len(array)):
#     prefix_sum.append(prefix_sum[i] + array[i])

# prefix_sum = [0 for _ in range(len(array) + 1)]
# for index in range(len(array)):
#     prefix_sum[index + 1] = prefix_sum[index] + array[index]

# print(prefix_sum)

array = [
    [1, 2, 3, 4, 5],
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
]

prefix_sum = [[0 for _ in range(len(array[0]) + 1)] for _ in range(len(array) + 1)]

for y in range(len(array)):
    for x in range(len(array[0])):
        prefix_sum[y + 1][x + 1] = array[y][x] - prefix_sum[y][x] + prefix_sum[y + 1][x] + prefix_sum[y][x + 1]

for i in range(len(prefix_sum)):
    print(prefix_sum[i])
