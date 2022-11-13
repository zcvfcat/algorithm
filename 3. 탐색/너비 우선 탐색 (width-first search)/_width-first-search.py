from collections import deque

graph = [[], [3, 4], [3, 4, 5], [1, 5], [1], [2, 6], [3, 5]]
visited = [False] * len(graph)
q = deque([1])


def queue_bfs(graph, visited, node):
    while q:
        node = q.popleft()

        if not visited[node]:
            print(node)
            visited[node] = True
            q.extend(graph[node])


queue_bfs(graph, visited, 1)
