from collections import deque


def solution(n, edges):
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    for node, edge in edges:
        graph[node].append(edge)
        graph[edge].append(node)

    q = deque([1])
    visited[1] = 1

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = visited[node] + 1
                q.append(edge)

    return visited.count(max(visited))


print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3)
