map_length, quiz_length = map(int, input().split(' '))

mini_map = [[0] * (map_length + 1)]
prefix_map = [[0] * (map_length + 1) for _ in range(map_length + 1)]

for i in range(map_length):
    mini_map.append([0] + list(map(int, input().split(' '))))

for i in range(1, map_length + 1):
    for j in range(1, map_length + 1):
        prefix_map[i][j] = mini_map[i][j] + prefix_map[i][j - 1] + \
            prefix_map[i - 1][j] - prefix_map[i - 1][j - 1]

for _ in range(quiz_length):
    x1, y1, x2, y2 = map(int, input().split(' '))
    ans = prefix_map[x2][y2] - prefix_map[x1 - 1][y2] - \
        prefix_map[x2][y1 - 1] + prefix_map[x1 - 1][y1 - 1]
    print(ans)
