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
    node_edge, node_weight = heapq.heappop(q)

    if distance[node_edge] < node_weight:
        continue

    for edge, edge_weight in graph[node_edge]:
        cost = node_weight + edge_weight

        if cost < distance[edge]:
            distance[edge] = cost
            heapq.heappush(q, (edge, cost))

for i in range(1, width + 1):
    if distance[i] != sys.maxsize:
        print(distance[i])
    else:
        print('INF')
