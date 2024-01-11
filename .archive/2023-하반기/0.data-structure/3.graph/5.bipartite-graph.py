"""
    이분 그래프
        노드 집합을 두 개의 그룹으로 나누어, 각 엣지가 두 그룹 간에만 연결
    
    사용 이유
        두 가지 다른 유형의 개체 또는 집합 간의 관계를 나타냄
            사용자와 상품, 작업과 리소스, 학생과 과목 등 상호 작용을 표현할때 유용
"""


class BipartiteGraph:
    def __init__(self):
        self.nodes_1 = set()
        self.nodes_2 = set()
        self.edges = set()

    def add_node(self, node, group):
        if group == 0:
            self.nodes_1.add(node)
        elif group == 1:
            self.nodes_2.add(node)

    def add_edge(self, node1, node2):
        if node1 in self.nodes_1 and node2 in self.nodes_2:
            self.edges.add((node1, node2))
        elif node2 in self.nodes_1 and node1 in self.nodes_2:
            self.edges.add((node2, node1))

bg = BipartiteGraph()

bg.add_node('A', 0)
bg.add_node('B', 0)
bg.add_node('X', 1)
bg.add_node('Y', 1)

bg.add_edge('A', 'X')
bg.add_edge('B', 'Y')

print(bg.nodes_1)
print(bg.nodes_2)
print(bg.edges)