from math import inf
from heapq import heappop, heappush


def dijkstra(graph, start, end):
    distance = [inf for _ in range(len(graph))]
    distance[start] = 0
    q = [(0, start)]

    while q:
        cost, node = heappop(q)
        print(cost, node)

        if distance[node] < cost:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if distance[edge] > next_cost:
                heappush((next_cost, edge))
                distance[edge] = next_cost

    return distance[end]


print(dijkstra([[(1, 2), (2, 3)], [(0, 1), (2, 3)], [(0, 2), (1, 3)]], 0, 2))
