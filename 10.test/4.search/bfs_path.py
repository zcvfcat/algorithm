from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 6, 8],
    [1, 4, 5],
    [3],
    [3],
    [2, 7],
    [6],
    [1, 2],
]


def bfs(graph, start_node):
    visited = [False for _ in range(len(graph))]
    start_path = [start_node]

    q = deque([start_path])
    visited[start_node] = True

    while q:
        path = q.popleft()
        node = path[-1]

        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                
                new_path = list(path)
                new_path.append(edge)
                q.append(new_path)

                if edge == len(graph) - 1:
                    return new_path

    return None

path = bfs(graph, 1)
print(path)