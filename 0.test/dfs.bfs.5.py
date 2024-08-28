from collections import deque


def bfs(graph: list[int], start, end):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        if node in visited:
            continue

        visited.add(node)
        for edge in graph[node]:
            queue.append((edge, path + [node]))

    return []


def dfs(graph: list[int], path: list[int], visited: set[int], node: int, end: int):
    if node == end:
        return path

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited:
            continue

        result = dfs(graph, path + [node], visited, neighbor, end)
        if result:
            return result
    return None