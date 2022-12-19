# 도시 도로 거리 출발번호
from collections import deque
n, m, k, x = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    city_1, city_2 = map(int, input().split())
    a[city_1].append(city_2)

visited = [-1] * (n + 1)
ans = []


def bfs(node):
    q = deque([node])
    visited[node] += 1

    while q:
        now = q.popleft()

        for edge in a[now]:
            if visited[edge] == -1:
                visited[edge] = visited[now] + 1
                q.append(edge)


bfs(x)

for i in range(n + 1):
    if visited[i] == k:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
