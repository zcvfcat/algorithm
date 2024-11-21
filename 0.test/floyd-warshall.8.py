from math import inf


def floyd_warshall(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    # 초기화
    for node in range(len(graph)):
        distances[node][node] = 0
        for edge, cost in graph[node]:
            distances[node][edge] = cost

    for route in range(len(graph)):
        for node in range(len(graph)):
            for neighbor in range(len(graph)):
                # 최단 거리 계산
                distances[node][neighbor] = min(
                    distances[node][neighbor], distances[node][route] + distances[route][neighbor])

    return distances


# Test Case 1: 간단한 그래프
graph1 = [
    [(1, 3), (2, 5)],
    [(0, 3), (2, 1)],
    [(0, 5), (1, 1)]
]
print("Test Case 1:")
print(floyd_warshall(graph1))
