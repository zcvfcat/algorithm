def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][i] + graph[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + graph[i][k]

    return dist