# GPT 생성
def dfs(graph: list[list[int]], target: int, node: int, visited: set[int]) -> bool:
    if node == target:
        return True

    visited.add(node)

    for edge in graph[node]:
        if edge not in visited:
            if dfs(graph, target, edge, visited):
                return True

    return False


def bfs(graph: list[list[int]], target: int) -> bool:
    visited = set()
    queue = [0]  # assuming the starting node is 0

    while queue:
        node = queue.pop(0)

        if node == target:
            return True

        if node not in visited:
            visited.add(node)
            for edge in graph[node]:
                queue.append(edge)

    return False

def run_tests():
    test_graphs = [
        [[1, 3], [0, 2], [1, 3], [0, 2]],  # 그래프 1
        [[1], [0, 2, 3], [1], [1, 4], [3]],  # 그래프 2
        [[1], [0, 2], [1], []]  # 그래프 3
    ]

    test_cases = [
        (0, 2, True, test_graphs[0]),
        (0, 4, False, test_graphs[0]),
        (0, 4, True, test_graphs[1]),
        (0, 3, False, test_graphs[2])
    ]

    for start_node, target, expected, graph in test_cases:
        dfs_result = dfs(graph, target, start_node, set())
        bfs_result = bfs(graph, target)
        print(f"Testing graph {graph}, target {target}")
        print(f"DFS result: {dfs_result}, expected: {expected}")
        print(f"BFS result: {bfs_result}, expected: {expected}")
        print()

run_tests()