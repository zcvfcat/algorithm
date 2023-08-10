from heapq import heappop, heappush, heapify
from math import inf


def dijkstra(graph, start):
    distance = [inf for _ in range(graph)]
    distance[start] = 0

    q = heapify([(0, start)])

    while q:
        cost, node = q.popleft()

        for edge, weight in graph[node]:
            current = cost + weight

            if distance[edge] > current:
                distance[edge] = current
                heappush(q, (current, edge))

    return distance