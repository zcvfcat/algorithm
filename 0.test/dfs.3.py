def dfs(graph: list[int], target: int, node: int, end: int, visited: set[int]) -> bool:
    if node == end:
        return True

    for edge in graph[node]:
        if edge in visited:
            continue

        visited.add(edge)
        if dfs(graph, target, edge, end, visited):
            return True

    return False