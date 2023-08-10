from collections import deque

def bfs(graph, start_node, end_node):
    visited = [0 for _ in range(len(graph))]
    q = deque([start_node])

    while q:
        node = q.popleft()

        if node == end_node:
            return visited

        for edge in graph[node]:
            if visited[edge] == 0:
                q += [edge]
                visited[edge] = visited[node] + 1
        
    return visited