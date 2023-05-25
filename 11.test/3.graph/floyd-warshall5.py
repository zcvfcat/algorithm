from math import inf


def floyd_warshall(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for i in range(len(distances)):
        distances[i][i] = 0

    for node in range(len(graph)):
        for edge, weight in graph[node]:
            distances[node][edge] = weight

    for route in range(len(graph)):
        for node in range(len(graph)):
            for edge in range(len(graph)):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])

    return distances

# 거리 2차 배열 만들어서 단순 업데이트
# 조건절 추가 필요함