"""
    사이클 그래프
        환형 구조를 가진 그래프
    
    사용 이유
        특정 상황에서의 주기적인 패턴, 반복, 순환적 현상등을 모델링할때 사용 - 주로 시계열
        주식 시장의 가격변동, 기상 패턴, 전력 수요 및 생태학적 상호작용, 경제적 주기 등을 이해하고 예측할때 사용
"""


class CycleGraph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def add_edge(self, node, edge):
        if 0 <= node < len(self.graph) and 0 <= edge < len(self.edge):
            self.graph[node].append(edge)
            self.graph[edge].append(node)
