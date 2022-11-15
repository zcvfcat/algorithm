INF = 1e8
width = 5
start = 1

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = [INF] * (width + 1)
visited = [False] * (width + 1)


def get_smallest_distance():
    min_weight = INF
    min_edge = 0

    for edge in range(1, width + 1):  # 방문 되지 않은 것들 중 가장 낮은 distance 찾기
        if distance[edge] < min_weight and not visited[edge]:
            min_weight = distance[edge]
            min_edge = edge
    return min_edge


def dijkstra(start_node):
    distance[start_node] = 0  # 시작 노드 0으로 초기화
    visited[start_node] = True

    for edge, weight in graph[start_node]:
        distance[edge] = weight  # 시작 노드와 인접 최단 거리 계산

    for _ in range(width - 1):  # 시작 노드를 제외 처리
        now_edge = get_smallest_distance()
        visited[now_edge] = True

        for next_edge, next_weight in graph[now_edge]:
            cost = distance[now_edge] + next_weight

            if cost < distance[next_edge]:
                distance[next_edge] = cost


dijkstra(start)
print(distance)
