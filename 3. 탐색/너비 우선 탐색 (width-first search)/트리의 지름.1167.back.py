from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
distance = [0] * (v + 1)

for _ in range(v):
    l = list(map(int, input().split(' ')))
    for i in range(1, len(l) - 2, 2):
        graph[l[0]].append((l[i], l[i + 1]))


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if visited[edge[0]] is True:
                continue

            visited[edge[0]] = True
            q.append(edge[0])
            distance[edge[0]] = distance[node] + edge[1]


bfs(1)

max_distance = 1

for i in range(2, v + 1):
    if distance[max_distance] < distance[i]:
        max_distance = i


visited = [False] * (v + 1)
distance = [0] * (v + 1)
bfs(max_distance)

distance.sort()
print(distance[v])
