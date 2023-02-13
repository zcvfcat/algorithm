from math import inf
import heapq

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

node_length = len(graph)
start_node = 1

distance = [inf for _ in range(node_length)]
distance[start_node] = 0

q = []
heapq.heappush(q, (0,start_node))

while q:
    prev_cost, node = heapq.heappop(q)

    if distance[node] < prev_cost:
        continue

    for edge, next_cost in graph[node]:
        cost = prev_cost + next_cost

        if distance[edge] > cost:
            distance[edge] = cost
            heapq.heappush(q, (cost,edge))

print(distance)