import sys
input = sys.stdin.readline

n = int(input())
maze = [[*map(int, input().rstrip())] for _ in range(n)]
txt = []


def dfs(y, x, n):
    check = maze[y][x]

    for h in range(y, y + n):
        for w in range(x, x + n):
            if check != maze[h][w]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dfs(y, x, n)
        dfs(y, x + n, n)
        dfs(y + n, x, n)
        dfs(y + n, x + n, n)
        print(")", end='')

    elif check == 1:
        print(1, end='')

    else:
        print(0, end='')


dfs(0, 0, n)
