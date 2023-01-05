# 17396
import heapq

INF = float('inf')

node_length, edge_length = map(int, input().split())
site = [INF]+[*map(int, input().split())]
graph = [[] for _ in range(node_length)]
distance = [INF for _ in range(node_length)]
path = [0 for _ in range(node_length)]
distance[0] = 0

for _ in range(edge_length):
    node, edge, weight = map(int, input().split())
    graph[node].append((edge, weight))

q = []
heapq.heappush(q, (0, 0))

while q:
    prev_cost, node = heapq.heappop()

    if distance[node] < prev_cost:
        continue

    for edge, cost in graph[node]:
        next_cost = cost + prev_cost

        if distance[edge] > next_cost:
            distance[edge] = next_cost
            heapq.heappush(q, (next_cost, edge))
