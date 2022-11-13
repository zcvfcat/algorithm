from collections import deque

n, m = map(int, input().split(' '))
array = []
visited = [[False] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(n):
    array.append(list(map(int, input())))


def vertify_in_boundary(y: int, x: int) -> bool:
    return y >= 0 and x >= 0 and y < n and x < m


def bfs(start_y: int, start_x: int):
    q = deque([(start_y, start_x)])

    while q:
        y, x = q.popleft()
        visited[y][x] = True

        for dy, dx in d:
            next_y = y + dy
            next_x = x + dx

            if not vertify_in_boundary(next_y, next_x):
                continue

            if array[next_y][next_x] == 0 or visited[next_y][next_x] is True:
                continue

            visited[next_y][next_x] = True
            array[next_y][next_x] = array[y][x] + 1

            q.append((next_y, next_x))


bfs(0, 0)

print(array[n - 1][m - 1])
