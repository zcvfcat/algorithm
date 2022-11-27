# 회전 구간 ㄷ 때문에 맵을 두배 늘려야함;;

from collections import deque

step = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def render(x1, y1, x2, y2):
    global minimap
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if x1 < x < x2 and y1 < y < y2:
                minimap[y][x] = 2
            elif minimap[y][x] != 2:
                minimap[y][x] = 1


def in_boundary(y, x):
    global height, width
    return y >= 1 and y < height and x >= 1 and x < width


def solution(rectangle, characterX, characterY, itemX, itemY):
    global minimap, height, width
    height = 102
    width = 102
    minimap = [[0 for _ in range(width)] for _ in range(height)]
    for x1, y1, x2, y2 in rectangle:
        render(x1 * 2, y1 * 2, x2 * 2, y2 * 2)

    visited = [[0 for _ in range(width)] for _ in range(height)]
    q = deque([(characterY * 2, characterX * 2)])
    visited[characterY * 2][characterX * 2] = 1

    while q:
        y, x = q.popleft()

        if y == itemY * 2 and x == itemX * 2:
            return (visited[y][x] - 1) // 2

        for dy, dx in step:
            ny = y + dy
            nx = x + dx

            if not in_boundary(ny, nx) or visited[ny][nx] != 0:
                continue

            if minimap[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] += visited[y][x] + 1


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8) == 17)
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1) == 11)
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7) == 9)
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10) == 15)
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3) == 10)
