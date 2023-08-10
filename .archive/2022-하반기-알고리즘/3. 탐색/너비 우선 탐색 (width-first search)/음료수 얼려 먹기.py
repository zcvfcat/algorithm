graph = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
]
height = len(graph)
width = len(graph[0])


def dfs(y, x):

    if x <= -1 or x >= width or y <= -1 or y >= height:
        return False

    if graph[y][x] == 0:
        graph[y][x] = 1

        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)

        return True

    return False


ans = 0

for i in range(height):
    for j in range(width):

        if dfs(i, j) == True:
            ans += 1

print(ans)
