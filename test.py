import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

step = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


def in_boundary(y, x):
    global w, h
    return 0 <= y < h and 0 <= x < w


def dfs(y,x):
    field[y][x] = 0
    for dy, dx in step:
        ny = y + dy
        nx = x + dx
        if in_boundary(ny, nx) and field[ny][nx] == 1:
            dfs(ny, nx)


while True:
    global w, h
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    field = []
    count = 0

    for _ in range(h):
        field.append(list(map(int, read().split())))

    for y in range(h):
        for x in range(w):
            if field[y][x] == 1:
                dfs(y, x)
                count += 1

    print(count)
