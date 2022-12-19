import sys
import heapq

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
distance = [sys.maxsize for _ in range(node_length + 1)]
visited = [False for _ in range(node_length + 1)]


def dijkstra(graph, start_node):
    distance[start_node] = 0
    q = []

    heapq.heappush(q, (start_node, 0))

    while q:
        vertex, acc_distance = heapq.heappop(q)

        if distance[vertex] > acc_distance:
            continue

        for edge, weight in graph[vertex]:
            cost = acc_distance + weight

            if distance[edge] > cost:
                distance[edge] = cost

                heapq.heappush(q, (edge, cost))
    return distance


print(dijkstra(graph, 1))
