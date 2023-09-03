"""
    사이클 그래프
"""


class CycleGraph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def add_edge(self, node, edge):
        if 0 <= node < len(self.graph) and 0 <= edge < len(self.edge):
            self.graph[node].append(edge)
            self.graph[edge].append(node)
