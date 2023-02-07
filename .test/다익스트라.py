from math import inf
from heapq import heappop, heappush

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

node_length = len(graph) - 1
start_node = 1


def dijkstra(graph, start_node):
    distance = [inf for _ in range(node_length + 1)]
    distance[start_node] = 0

    q = []
    heappush(q, (0, start_node))

    while q:
        weight, node = heappop(q)

        if distance[node] < weight:
            continue
            
        for edge, cost in graph[node]:
            total = cost + weight

            if distance[edge]> total:
                distance[edge] = total
                heappush(q,(total, edge))

    return distance


print(dijkstra(graph, start_node))
