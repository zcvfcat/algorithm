INF = float('inf')


def floyd_warshall(graph):
    l = len(graph)
    dist = [[INF] * l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for route in range(l):
        for node in range(l):
            for edge in range(l):
                dist[node][edge] = min(dist[node][edge], dist[node][route] + dist[route][edge])
    return dist


graph = [
    [0, 2, 5, INF],
    [2, 0, INF, 4],
    [5, INF, 0, 1],
    [INF, 4, 1, 0]
]

dist = floyd_warshall(graph)