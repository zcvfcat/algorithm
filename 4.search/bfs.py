from collections import deque


def bfs(graph, start, goal):
    queue = deque()
    queue.append(start)

    visited = set()
    visited.add(start)

    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    return path


graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'D'],
         'D': ['B', 'C']}

print(bfs(graph, 'A', 'D'))
