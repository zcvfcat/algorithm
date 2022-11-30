import sys
import heapq

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

node_length = len(graph) - 1
start_node = 1
distance = [sys.maxsize for _ in range(node_length + 1)]
visited = [False for _ in range(node_length + 1)]

distance[1] = 0
q = []
heapq.heappush(q, (start_node, 0))

while q:
    node, node_weight = heapq.heappop(q)

    if distance[node] > node_weight:
        continue

    for edge, edge_weight in graph[node]:
        cost = node_weight + edge_weight

        if distance[edge] > cost:
            distance[edge] = cost

            heapq.heappush(q, (edge,cost))

print(distance)