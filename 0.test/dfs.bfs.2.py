from collections import deque


def dfs(graph, node, end, visited):
    if node == end:
        return node

    visited[node] = True

    for edge in graph[node]:
        if not visited[edge] and dfs(graph, edge, end, visited):
            return True

    return False


def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()
        visited.add(node)
        path.append(node)

        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path[:]))

    return []
