import sys


def bellman_ford(graph, start):
    # 그래프의 모든 정점의 거리 값을 무한대로 초기화
    distance = {node: float('inf') for node in graph}
    # 시작 정점의 거리를 0으로 설정
    distance[start] = 0

    # 모든 정점에 대해 최단 경로를 계산
    for i in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    # 음수 가중치 사이클이 있는지 검사
    for u in graph:
        for v, w in graph[u].items():
            if distance[u] + w < distance[v]:
                print("음수 가중치 사이클이 존재합니다.")
                return

    # 결과 출력
    print("최단 거리:")
    for node, dist in distance.items():
        print(node, ":", dist)


graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

bellman_ford(graph, 'A')
