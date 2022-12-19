import sys

width = 5
start_node = 1

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = [sys.maxsize] * (width + 1)
visited = [False] * (width + 1)


def get_smallest_distance():
    min_weigth = sys.maxsize
    min_edge = 0

    for edge in range(1, width + 1):
        if distance[edge] < min_weigth and not visited[edge]:
            min_weigth = distance[edge]
            min_edge = edge

    return min_edge


def dijkstra(graph, distance, start_node):
    distance[start_node] = 0
    visited[start_node] = True

    for edge, edge_weight in graph[start_node]:
        distance[edge] = edge_weight

    for i in range(width - 1):
        node = get_smallest_distance()
        visited[node] = True

        for edge, edge_weight in graph[node]:
            cost = distance[node] + edge_weight

            if cost < distance[edge]:
                distance[edge] = cost


dijkstra(graph, distance, start_node)
print(distance)
