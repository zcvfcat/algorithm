def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, end, visited, path)
            if result is not None:
                return result

    path.pop()
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
end = 'F'

path = dfs(graph, start, end)

if path is not None:
    print(f"경로: {' -> '.join(path)}")
else:
    print("경로가 존재하지 않습니다.")
