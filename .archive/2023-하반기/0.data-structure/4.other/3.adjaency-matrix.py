"""
    인접 행렬
        그래프를 행렬로 나타내며, 노드 간의 연결 여부를 표현하는 자료구조

    사용 이유
        빠른 엣지 검색
        엣지 가중치 표현
        무방향 그래프 지원
        그래프 크기 고정
        그래프 탐색
            너비 우선 탐색, 다익스트라 알고리즘
        행렬 연산
        !!희소 그래프 제외
"""

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]  # 인접 행렬 초기화

    def add_edge(self, node, edge, weight = 1):
        if 0 <= node < self.size and 0 <= edge < self.size:
            self.adj_matrix[node][edge] = weight

    def remove_edge(self, node, edge):
        if 0 <= node < self.size and 0 <= edge < self.size:
            self.adj_matrix[node][edge] = 0

    def is_edge(self, node, edge):
        if 0 <= node < self.size and 0 <= edge < self.size:
            return self.adj_matrix[node][edge] != 0
        return False


graph = Graph(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

graph.remove_edge(1, 2)

print(graph.is_edge(0, 1))
print(graph.is_edge(1, 2))
