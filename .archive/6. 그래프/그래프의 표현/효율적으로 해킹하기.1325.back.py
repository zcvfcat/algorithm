import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
visited = [False] * n
ans = [0] * (n + 1)

for _ in range(m):
    node, edge = map(int, input().split())
    a[node].append(edge)


def bfs(started_node):
    q = deque([started_node])
    visited[started_node] = True

    while q:
        node = q.popleft()

        for edge in a[node]:
            if not visited[edge]:
                visited[edge] = True
                ans[edge] += 1
                q.append(edge)


for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

max_edge = 0

for i in range(1, n + 1):
    max_edge = max(max_edge, ans[i])

for i in range(1, n + 1):
    if max_edge == ans[i]:
        print(i, end=' ')
