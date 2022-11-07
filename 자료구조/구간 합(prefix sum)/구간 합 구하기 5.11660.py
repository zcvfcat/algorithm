n, quiz_length = map(int, input().split(' '))

mini_map = [[0] * (n + 1)]
prefix_map = [[0] * (n + 1)] * (n + 1)

for i in range(n):
    mini_map.append([0] + list(map(int, input().split(' '))))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_map[i][j] = prefix_map[i][j-1] + \
            prefix_map[i-1][j] - prefix_map[i-1][j-1] + mini_map[i][j]
