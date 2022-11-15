import sys
import heapq

input = sys.stdin.readline

width = int(input())
edge_range = int(input())

graph = [[] for _ in range(width + 1)]
distance = [sys.maxsize] * (width + 1)

for _ in range(edge_range):
    node, edge, node_weight = map(int, input().split())
    graph[node].append((edge, node_weight))

start_node, end_node = map(int, input().split())

q = []
heapq.heappush(q, [start_node, 0])
distance[start_node] = 0

while q:
    node, node_weight = heapq.heappop(q)

    if distance[node] < node_weight:
        continue

    for edge, edge_weight in graph[node]:
        cost = distance[node] + edge_weight

        if cost < distance[edge]:
            distance[edge] = cost
            heapq.heappush(q, (edge, cost))

print(distance[end_node])
