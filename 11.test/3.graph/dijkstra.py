import heapq
import math


def dijkstra(graph, start):
    distances = [math.inf for _ in range(len(graph))]
    distances[start] = 0

    q = [(0, start)]

    while q:
        dist, node = heapq.heappop(q)

        if dist > distances[node]:
            continue

        for edge, weight in graph[node]:
            next = weight + dist

            if distances[edge] > next:
                distances[edge] = next
                heapq.heappush(q, (next, edge))

    return distances
