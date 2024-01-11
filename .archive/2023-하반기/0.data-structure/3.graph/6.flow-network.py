"""
    플로우 네트워크 - 공부 아직 안되어 있음...
        자원의 흐름과 관련된 네트워크
        최대 흐름을 찾거나 최적 경로를 결정하는 데 사용
    
    사용 이유
        네트워크 최적화 문제 해결
            최대 흐름 문제를 푸는 데 사용
            정보, 자원, 물류 등 최대 흐름을 찾는 것
            교통 최적화, 통신 네트워크 최적 경로, 전력 네트워크 최적 용량 할당
"""


class FlowNetwork:
    def __init__(self):
        self.graph = {}
        self.source = None
        self.sink = None

    def add_edge(self, u, v, capacity):
        """
        엣지를 추가합니다.

        :param u: 출발 노드
        :param v: 도착 노드
        :param capacity: 엣지의 용량
        """
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}

        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # 역방향 엣지 초기화 (역방향으로의 흐름은 0)

    def set_source_sink(self, source, sink):
        """
        원천과 싱크 노드를 설정합니다.

        :param source: 원천 노드
        :param sink: 싱크 노드
        """
        self.source = source
        self.sink = sink

    def find_path(self):
        """
        원천에서 싱크로 가는 경로를 찾습니다.

        :return: 경로가 있으면 경로를 반환하고, 없으면 None을 반환
        """
        visited = set()
        stack = [self.source]
        while stack:
            node = stack.pop()
            visited.add(node)
            for neighbor, capacity in self.graph[node].items():
                if neighbor not in visited and capacity > 0:
                    stack.append(neighbor)
                    if neighbor == self.sink:
                        path = []
                        current = self.sink
                        while current != self.source:
                            path.append(current)
                            current = stack[-1]
                        path.append(self.source)
                        path.reverse()
                        return path
        return None

    def max_flow(self):
        """
        최대 흐름을 계산합니다.

        :return: 최대 흐름 값
        """
        if self.source is None or self.sink is None:
            raise ValueError("원천과 싱크를 설정해야 합니다.")

        flow = 0
        path = self.find_path()
        while path:
            # 경로 상에서 최소 용량을 찾음
            min_capacity = float("inf")
            for u, v in zip(path, path[1:]):
                min_capacity = min(min_capacity, self.graph[u][v])

            # 경로 상의 각 엣지에 최소 용량만큼 흐름을 더함
            for u, v in zip(path, path[1:]):
                self.graph[u][v] -= min_capacity
                self.graph[v][u] += min_capacity

            flow += min_capacity
            path = self.find_path()

        return flow


# 플로우 네트워크 인스턴스 생성
fn = FlowNetwork()

# 엣지 추가
fn.add_edge('S', 'A', 10)
fn.add_edge('S', 'B', 5)
fn.add_edge('A', 'C', 15)
fn.add_edge('B', 'C', 10)
fn.add_edge('A', 'D', 10)
fn.add_edge('C', 'T', 10)
fn.add_edge('D', 'T', 15)

# 원천과 싱크 설정
fn.set_source_sink('S', 'T')

# 최대 흐름 계산
max_flow_value = fn.max_flow()
print("최대 흐름:", max_flow_value)
