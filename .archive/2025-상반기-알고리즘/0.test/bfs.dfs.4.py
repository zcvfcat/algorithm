from collections import deque

def bfs(graph, start, end):
    visited = set()
    visited.add(start)

    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path
        
        for neighbor in graph[node]:
            if neighbor in visited:
                continue

            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))

    return None

def dfs(graph, visited, start, end):
    if start == end:
        return [start]

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, visited, neighbor, end)
            if path:
                return [start] + path

    visited.remove(start)
    return []