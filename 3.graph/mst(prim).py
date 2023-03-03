import heapq

def prim(graph, start):
    # 시작 정점에서부터 연결된 노드와 가중치를 저장할 큐 
    connected_edge_queue = [(0, start)]
    # 이미 방문한 정점들의 집합 
    visited = set()
    
    while connected_edge_queue:
        # 가장 작은 가중치를 가져옴 
        weight, node = heapq.heappop(connected_edge_queue)
        if node not in visited:
            visited.add(node)
            yield (weight, node)
            # 새롭게 연결된 선분과 그에 대한 정보를 큐에 추가함 
            for edge in graph[node]:
                if edge[1] not in visited:
                    heapq.heappush(connected_edge_queue, edge)

# 위 함수 prim은 다음과 같은 parameter를 받습니다.
# graph: 인접 리스트로 표현된 그래프
# start: 시작 정점
# 해당 함수는 모든 연결된 정점들을 찾아 그래프를 최소 비용으로 탐색하여 주어진 그래프에서의 Minimum Spanning Tree(MST)의 가중치를 출력합니다.