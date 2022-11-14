from collections import deque
a, b, c = map(int, input().split(' '))

visited = [[False for _ in range(201)] for _ in range(201)]
ans = [False] * 201


def bfs():
    q = deque([(0, 0)])
