from heapq import heappush, heappop
from math import inf


def dijkstra(graph, start):
    distances = [inf for _ in range(len(graph))]

    q = [(0, start)]

    while q:
        cost, node = heappop(q)

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if distances[edge] > next_cost:
                distances[edge] = next_cost
                heappush(q, (next_cost, edge))

    return distances