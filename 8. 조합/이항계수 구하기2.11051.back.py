# 이항계수
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(0, n + 1):
    d[i][1] = i
    d[i][0] = 1
    d[i][i] = 1

for i in range(2, n + 1):
    for j in range(1, i):
        d[i][j] = (d[i - 1][j] + d[i - 1][j - 1]) % 10007

print(d[n][k])

# from math import factorial

# n,k = map(int,input().split())
# v = factorial(n) // (factorial(k) * factorial(n-k))

# print(v%10007)
