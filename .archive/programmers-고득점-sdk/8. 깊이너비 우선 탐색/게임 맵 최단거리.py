from collections import deque

step = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_boundary(y, x):
    global height, width
    return y >= 0 and y < height and x >= 0 and x < width


def solution(maps):
    global height, width

    height = len(maps)
    width = len(maps[0])

    visited = [[False for _ in range(width)] for _ in range(height)]

    q = deque([(0, 0, 1)])
    visited[0][0] = True

    cnt = -1

    while q:
        y, x, count = q.popleft()

        if y == (height - 1) and x == (width - 1):
            cnt = count
            break

        for dy, dx in step:
            next_y = y + dy
            next_x = x + dx

            if in_boundary(next_y, next_x) and maps[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                visited[next_y][next_x] = True
                q.append((next_y, next_x, count + 1))

    return cnt


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11)
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1)
