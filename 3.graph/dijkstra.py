"""
    다익스트라
        시작 노로 부터 각 노드까지 최단 경로를 찾는 알고리즘

    시간 복잡도
        검색
            배열 사용시 O(VE)
            우선순위 큐를 사용시 O(V log2E)

    사용 이유
        단일 출발 지점에서 다른 모든 노드까지의 최단 경로를 구할 때
            다익스트라 알고리즘은 하나의 출발 노드에서 다른 모든 노드까지의 최단 경로를 효율적으로 찾음
            ex) 도로 네트워크에서 특정 위치에서 다른 모든 위치까지의 최단 거리를 찾을 때 사용

        가중치가 양수인 그래프에서 사용
            다익스트라 알고리즘은 음수 가중치를 갖는 간선이 없는 경우에만 정확한 결과를 제공
            음수 가중치를 다루려면 벨먼-포드 알고리즘과 같은 다른 알고리즘을 사용

        간선의 수가 적은 밀집 그래프에서 사용
            다익스트라는 간선의 수가 적은 밀집 그래프에서 빠른 실행 속도를 가짐
            간선의 수가 매우 많은 희소 그래프의 경우에는 효율성이 떨어짐
"""

from heapq import heappush, heappop
from math import inf


def dijkstra(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0
    q = []

    heappush(q, (0, start_node))

    while q:
        cost, node = heappop(q)

        if distance[node] < cost:
            continue

        for edge, weight in graph[node]:
            next_cost = cost + weight

            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush(q, (next_cost, edge))
    return distance