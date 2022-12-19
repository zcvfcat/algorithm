# 모르겠음...

import sys
input = sys.stdin.readline

f = [0] * 21
s = [0] * 21
visited = [False] * 21

n = int(input())
f[0] = 1

for i in range(1, n + 1):
    f[i] = f[i - 1] * i
