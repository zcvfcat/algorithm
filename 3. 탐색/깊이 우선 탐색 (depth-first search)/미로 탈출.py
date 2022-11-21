from collections import deque

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

# 초기화
height = len(graph)
width = len(graph[0])
end = (height - 1, width - 1)
start = (0, 0)
visited = [[False for _ in range(width)] for _ in range(height)]
path_length = 1

q = deque([(*start, path_length)])
step = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# 바운더리 검증
def in_boundary(y, x):
    return x >= 0 and x < width and y >= 0 and y <= height


# bfs
while q:
    y, x, path_length = q.popleft()

    if (y, x) == end:
        break

    for dy, dx in step:
        next_y, next_x = y + dy, x + dx

        if not in_boundary(next_y, next_x) or visited[y][x] == True or graph[y][x] == 0:
            continue

        q.append((next_y, next_x, path_length + 1))

print(path_length)
