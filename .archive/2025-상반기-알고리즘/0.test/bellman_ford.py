from math import inf


def bellman_ford(edges, start, node_length):
    distance = [inf for _ in range(node_length)]
    distance[start] = 0

    for i in range(node_length - 1):  # node_length-1번 반복
        for node, edge, weight in edges:
            cost = distance[node] + weight
            if distance[node] != inf and distance[edge] > cost:
                distance[edge] = cost

    # 음수 가중치 사이클 체크
    for node, edge, weight in edges:
        cost = distance[node] + weight
        if distance[node] != inf and distance[edge] > cost:
            return True  # 음수 사이클이 존재함

    return False  # 음수 사이클이 없음


# 그래프 정의 및 실행 예시
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

# 음수 가중치 사이클 유무 확인
has_negative_cycle = bellman_ford(edges, 0, 5)
if has_negative_cycle:
    print("Graph contains negative weight cycle")
else:
    print("No negative weight cycle found")
