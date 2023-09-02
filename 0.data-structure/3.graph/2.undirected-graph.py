"""
    무방향 그래프
        정점들 간의 연결 관계를 나타내는 그래프로, 간선에 방향성이 없는 자료 구조

    시간 복잡도
        정점 추가 (add_vertex): O(1)
        간선 추가 (add_edge): O(1)
        정점 제거 (remove_vertex): O(V)
        간선 제거 (remove_edge): O(E)
    
    사용 이유
        네트워크 모델링
            컴퓨터 네트워크, 소셜 네트워크, 전력 공급망 등을 모델링 할 경우
            노드의 엔티티 (컴퓨터, 사람, 전력 스테이션)
            간선의 엔티티 (네트워크 연결, 친구 관계, 전력 전달)
        알고리즘 및 데이터 구조 연구
            경로 찾기, 최단 경로, 연결 요소 검색, 그래프 순회
            
"""

class UnDirectGraph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.graph and vertex_2 in self.graph:
            if vertex_2 not in self.graph[vertex_1]:
                self.graph[vertex_1].append(vertex_2)

            if vertex_1 not in self.graph[vertex_2]:
                self.graph[vertex_2].append(vertex_1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]

            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.graph and vertex_2 in self.graph:
            if vertex_2 in self.graph[vertex_1]:
                self.graph[vertex_1].remove(vertex_2)

            if vertex_1 in self.graph[vertex_2]:
                self.graph[vertex_2].remove(vertex_1)

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

