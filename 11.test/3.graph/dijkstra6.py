from heapq import heappop, heappush
from math import inf


def dijkstra(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    q = [(0,start_node)]

    while q:
        cost, node=heappop(q)

        for weight, edge in graph[node]:
            next_cost = cost + weight

            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush(q, (next_cost, edge))
    
    return distance
