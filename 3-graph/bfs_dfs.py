from collections import deque


def bfs(graph, start):
    """
    너비 우선 탐색(BFS).

    - 입력: graph는 인접 리스트(dict: node -> iterable of neighbors), start는 시작 정점
    - 반환: (탐색 순서 리스트, 부모 딕셔너리)

    예시:
        graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: []}
        order, parent = bfs(graph, 0)
    """
    visited = set()
    order = []
    parent = {start: None}
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    return order, parent


def dfs_iterative(graph, start):
    """
    깊이 우선 탐색(DFS, 반복문/스택 버전).

    - 입력: graph는 인접 리스트(dict), start는 시작 정점
    - 반환: (탐색 순서 리스트, 부모 딕셔너리)
    """
    visited = set()
    order = []
    parent = {start: None}
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        neighbors = list(graph.get(node, []))
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = node
                stack.append(neighbor)

    return order, parent


def dfs_recursive(graph, start):
    """
    깊이 우선 탐색(DFS, 재귀 버전).

    - 입력: graph는 인접 리스트(dict), start는 시작 정점
    - 반환: (탐색 순서 리스트, 부모 딕셔너리)
    """
    visited = set()
    order = []
    parent = {start: None}

    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                _dfs(v)

    _dfs(start)
    return order, parent


