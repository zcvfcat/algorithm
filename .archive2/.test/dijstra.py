from math import inf
from heapq import heappush, heappop

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]


def dijkstra(start_node, graph):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0
    heap = []

    heappush(heap, ((distance[start_node], start_node)))

    while heap:
        cost, node = heappop(heap)

        if distance[node] < cost:
            continue

        for edge, next_cost in graph[node]:
            maybe_cost = cost + next_cost

            if distance[edge] > maybe_cost:
                distance[edge] = maybe_cost
                heappush(heap, (maybe_cost, edge))

    return distance


print(dijkstra(1, graph))
