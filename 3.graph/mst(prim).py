import sys


def prim(graph, start):
    # 모든 정점의 거리 값을 무한대로 초기화
    distance = {node: sys.maxsize for node in graph}
    # 시작 정점의 거리를 0으로 설정
    distance[start] = 0
    # 시작 정점부터 시작
    current = start
    # 방문한 노드들을 저장할 집합
    visited = set()
    # 최소 신장 트리를 저장할 리스트
    mst = []

    while len(visited) < len(graph):
        visited.add(current)

        # 현재 정점과 연결된 모든 정점에 대해
        for neighbor, weight in graph[current].items():
            # 이미 방문한 정점은 건너뜀
            if neighbor in visited:
                continue
            # 현재까지의 거리보다 더 가까운 거리가 있다면 업데이트
            if weight < distance[neighbor]:
                distance[neighbor] = weight

        # 가장 짧은 거리의 정점을 선택
        next_node = min(distance, key=distance.get)
        # 현재 정점과 선택된 정점을 연결하는 간선을 최소 신장 트리에 추가
        mst.append((current, next_node, distance[next_node]))
        # 선택된 정점을 현재 정점으로 변경
        current = next_node
        # 선택된 정점의 거리 값을 무한대로 변경하여 다시 선택되지 않도록 함
        distance[next_node] = sys.maxsize

    # 결과 출력
    print("최소 신장 트리: ")
    for edge in mst:
        print(edge[0], "-", edge[1], ":", edge[2])


graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5, 'F': 8},
    'D': {'A': 5, 'B': 9, 'E': 15},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 9, 'G': 11},
    'F': {'C': 8, 'E': 9, 'G': 10},
    'G': {'E': 11, 'F': 10}
}

prim(graph, 'A')
