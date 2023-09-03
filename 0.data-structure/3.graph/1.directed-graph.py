"""
    방향 그래프
        정점들 간의 연결 관계를 나타내는 그래프로, 간선에 방향성이 없는 자료 구조
    
    시간 복잡도
        정점 추가 (add_vertex): O(1)
        간선 추가 (add_edge): O(1)
        정점 제거 (remove_vertex): O(V)
        간선 제거 (remove_edge): O(E)

    사용 이유
        네트워크 모델링
            웹의 하이퍼 링크 구조, 도로 네트워크, 데이터 흐름
        알고리즘 및 데이터 구조 연구
            최단 경로, 위상 정렬, 그래프 순회 등 문제 해결
"""

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                self.graph[v] = [neighbor for neighbor in self.graph[v] if neighbor != vertex]

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph:
            if to_vertex in self.graph[from_vertex]:
                self.graph[from_vertex].remove(to_vertex)

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []