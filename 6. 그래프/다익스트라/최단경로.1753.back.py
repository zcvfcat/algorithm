import heapq
import sys
input = sys.stdin.readline

width, edge_length = map(int, input().split())
start = int(input())
graph = [[] for _ in range(width + 1)]
distance = [sys.maxsize] * (width + 1)
visited = [False] * (width + 1)

for edge_length in range(edge_length):
    node, edge, weight = map(int, input().split(' '))
    graph[node].append((edge, weight))

q = []

heapq.heappush(q, (start, 0))
distance[start] = 0

while q:
    now_edge, now_weight = heapq.heappop(q)

    if distance[now_edge] < now_weight:
        continue

    for next_edge, next_weight in graph[now_edge]:
        cost = distance[now_edge] + next_weight

        if cost < distance[next_edge]:
            distance[next_edge] = cost
            heapq.heappush(q, (next_edge, cost))

for i in range(1, width + 1):
    if distance[i] != sys.maxsize:
        print(distance[i])
    else:
        print('INF')
