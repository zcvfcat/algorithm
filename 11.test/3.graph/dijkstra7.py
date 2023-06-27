from math import inf
from heapq import heappop, heappush


def dijkstra(graph: list, start: int, end: int):
    distances = [inf for _ in range(len(graph))]
    distances[start] = 0

    q = [(0, start)]

    while q:
        cost, node = heappop(q)

        if cost > distances[node]:
            continue

        for weight, edge in graph[node]:
            next_weight = weight + cost

            if distances[edge] > next_weight:
                distances[edge] = next_weight
                heappush(q, (next_weight, edge))

    return distances
