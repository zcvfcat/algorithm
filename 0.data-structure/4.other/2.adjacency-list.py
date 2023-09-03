"""
    인접 리스트
        효율적으로 표현하기 위해 각 노드가 인접한 다른 노드들의 리스트를 저장하는 자료구조

    사용 이유
        메모리 효율성
            희소 그래프(Sparse Graph)를 표현
            연결된 노드만 저장으로 메모리 낭비 줄임
        빠른 인접 노드 접근
            인접한 노드를 빠르게 찾기 위함
        삽입 및 삭제 연산의 효율성
            노드나 엣지를 추가 시, 인접 리스트에서 연산만 수행하면 됨
        그래프의 표현 간결성
            각 노드마다 인접한 노드 리스트를 가지고 있으므로 그래프의 구조를 직관적으로 파악
        효율적인 메모리 사용
            그래프가 크더라도 적은 메모리를 사용
        그래프 유형에 유연성
            다양한 그래프 유형을 표현 할 수 있음, 무방향 그래프, 방향 그래프, 가중치 그래프

"""

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return []


graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

print("A의 인접한 노드:", graph.get_neighbors('A'))
print("B의 인접한 노드:", graph.get_neighbors('B'))
print("C의 인접한 노드:", graph.get_neighbors('C'))
print("D의 인접한 노드:", graph.get_neighbors('D'))

print("\n그래프 정보:")
print(graph)
