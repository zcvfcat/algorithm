from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_boundary(h, w, y, x):
    return 0 <= y < h and 0 <= x < w

def bfs(maze, visited, h, w, start_y, start_x):
    q = deque([(start_y, start_x)])
    visited[start_y][start_x] = True

    count = int(maze[start_y][start_x])

    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = dy + y, dx + x

            if in_boundary(h, w, ny, nx) and visited[ny][nx] is False and maze[ny][nx] is not 'X':
                visited[ny][nx] = True
                count += int(maze[ny][nx])
                q.append((ny, nx))

    return count


def solution(maze):
    h, w = len(maze), len(maze[0])
    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = []

    for y in range(h):
        for x in range(w):
            if maze[y][x] is not 'X' and visited[y][x] is False:
                count = bfs(maze, visited, h, w, y, x)
                ans.append(count)

    return sorted(ans) if ans else [-1]



print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]) == [1, 1, 27])
print(solution(["XXX", "XXX", "XXX"]) == [-1])
