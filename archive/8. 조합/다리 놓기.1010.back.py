import sys

input = sys.stdin.readline
d = [[0 for j in range(31)] for _ in range(31)]

for i in range(0, 31):
    d[i][1] = i
    d[i][0] = 1
    d[i][i] = 1

for i in range(2, 31):
    for j in range(1, i):
        d[i][j] = d[i - 1][j] + d[i - 1][j - 1]

t = int(input())

for _ in range(0, t):
    n, m = map(int, input().split())
    print(d[m][n])
