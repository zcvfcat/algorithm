from math import inf


def floyd(graph):
    distances = [[inf] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
        distances[i][i] = 0

    for edge, weight in graph.items():
        start, end = edge
        distances[start][end] = weight
        distances[end][start] = weight

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j])

    return distances
