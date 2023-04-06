from heapq import heappush, heappop
from math import inf

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]


def dijkstra(graph: list, start_node: int = 1):
    distance = [inf for _ in range(len(graph))]

    q = [(0, start_node)]
    distance[start_node] = 0

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


dist = dijkstra(graph, 1)
print(dist)
