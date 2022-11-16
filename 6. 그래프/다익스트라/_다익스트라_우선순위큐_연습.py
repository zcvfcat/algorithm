import sys
import heapq

width = 5
start = 1

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = [sys.maxsize] * (width + 1)


def dijkstra(graph, distance, start):
    distance[start] = 0
    q = []

    heapq.heappush(q, (start, 0))

    while q:
        node, node_weight = heapq.heappop(q)

        if distance[node] > node_weight:
            continue

        for edge, edge_weight in graph[node]:
            cost = node_weight + edge_weight

            if distance[edge] > cost:
                distance[edge] = cost
                heapq.heappush(q, (edge, cost))


dijkstra(graph, distance, start)
print(distance)
