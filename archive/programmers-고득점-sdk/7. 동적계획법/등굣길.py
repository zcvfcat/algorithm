def solution(width, height, puddles):
    prefix_sum = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    prefix_sum[1][1] = 1

    for y in range(1, height + 1):
        for x in range(1, width + 1):
            if y == 1 and x == 1:
                continue

            if [x, y] in puddles:
                prefix_sum[y][x] = 0
                continue

            prefix_sum[y][x] = (prefix_sum[y - 1][x] + prefix_sum[y][x - 1]) % 1_000_000_007

    return prefix_sum[y][x]


print(solution(4,	3,	[[2, 2]]) == 4)
