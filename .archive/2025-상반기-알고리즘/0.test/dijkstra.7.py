from heapq import heappush, heappop
from math import inf


# 자료구조 그래프 node: (edge, weight)
def dijkstra(graph: list[(int, int)], start, end):
    distance = [inf for _ in range(len(graph))]
    q = [(0, start)]

    while q:
        cost, node = heappop(q)

        if distance[node] < cost:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush(q, (next_cost, edge))

    return distance
