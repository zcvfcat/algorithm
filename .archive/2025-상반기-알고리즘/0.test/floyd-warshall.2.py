from math import inf


def floyd_warshall(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for node in range(len(graph)):
        # 자기자신 초기화
        distances[node][node] = 0

        # 연결된 선분 cost 추가
        for cost, edge in graph[node]:
            distances[node][edge] = cost

    for route in range(len(graph)):
        for node in range(len(graph)):
            for edge in range(len(graph)):
                # 목적지까지 cost 비교 후, 더 가까운 것 넣기
                distances[node][edge] = min(
                    distances[node][edge], distances[node][route] + distances[route][edge])

    return distances
