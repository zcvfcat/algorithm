import heapq
import math


def astar(graph, start, goal):
    # 시작 정점에서의 거리 값을 0으로 초기화
    distance = {node: math.inf for node in graph}
    distance[start] = 0

    # 휴리스틱 함수를 이용하여 각 정점에서 목표 정점까지의 예상 거리를 계산
    h = {node: heuristic(node, goal) for node in graph}

    # 시작 정점부터 탐색을 시작
    queue = [(start, 0)]

    while queue:
        # 탐색할 정점 중 거리가 가장 짧은 정점 선택
        current, cost = heapq.heappop(queue)

        # 이미 최단 경로를 찾은 경우, 탐색을 중지
        if current == goal:
            break

        # 인접한 정점에 대해 탐색을 수행
        for neighbor, weight in graph[current].items():
            # 시작 정점부터 현재 정점까지의 거리와 현재 정점에서 인접한 정점까지의 가중치를 더하여 인접한 정점까지의 거리를 계산
            dist = distance[current] + weight

            # 현재까지 계산된 거리보다 더 짧은 거리가 발견된 경우, 거리 값을 업데이트하고 우선순위 큐에 추가
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                priority = dist + h[neighbor]
                heapq.heappush(queue, (neighbor, priority))

    # 경로 추적
    path = []
    while current != start:
        path.append(current)
        current = min(graph[current], key=lambda node: distance[node] + h[node])
    path.append(start)
    path.reverse()

    return path, distance[goal]


def heuristic(node, goal):
    # 각 노드간의 유클리드 거리를 휴리스틱 함수로 사용
    (x1, y1) = node
    (x2, y2) = goal
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# 테스트 코드
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (2, 2): 3},
    (2, 2): {(1, 1): 3}
}

start = (0, 0)
goal = (2, 2)

path, distance = astar(graph, start, goal)

print(path, distance)
