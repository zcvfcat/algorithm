"""
    가중치 그래프
        연결된 항목 간의 상대적인 중요성을 표현하는 그래프
    
    시간 복잡도
        최단 경로 알고리즘
            다익스트라 알고리즘 O(VE) or O(log2(V) * E)
            벨만-포드 알고리즘 O(VE)
        최소 신장 트리 알고리즘
            크루스칼 알고리즘 O(E * log(E)) - 인접 행렬
            프림 알고리즘 O(VE)
        네트워크 플로우 알고리즘
            에드몬즈-카프 알고리즘 O(V^3 * E)
    
    사용 이유
        경로 및 최단 경로 문제
            노드 및 엣지에 가중치를 활당
            네트워크 라우팅, GPS 네비게이션, 통신 네트워크 최적 경로
        네트워크 흐름
            엣지의 용량과 흐름을 고려하여 데이터 또는 자원의 최적 분배를 결정
            최대 흐름 문제, 최소 절단 문제
        그래프 알고리즘
            최소 신장 트리, 최단 경로 알고리즘, 네트워크 플로우 알고리즘
"""

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        self.graph[vertex2][vertex1] = weight  # 무방향 그래프인 경우

    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return {}