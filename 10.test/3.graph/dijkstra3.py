from math import inf
from heapq import heappush, heappop


def dijkstra(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0
    
    q = []
    heappush(q, (0, start_node))

    while q:
        cost, node = heappop(q)

        if distance[node] < cost:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if distance[edge] > next_cost:
                heappush(q, (next_cost, edge))
                distance[edge] = next_cost

    return distance

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

dist = dijkstra(graph, 1)
print(dist)