INF = float('inf')


def floyd_warshall(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]

    # 초기화
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    # Floyd-Warshall 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


graph = [
    [0, 2, 5, INF],
    [2, 0, INF, 4],
    [5, INF, 0, 1],
    [INF, 4, 1, 0]
]

dist = floyd_warshall(graph)

for row in dist:
    print(row)
