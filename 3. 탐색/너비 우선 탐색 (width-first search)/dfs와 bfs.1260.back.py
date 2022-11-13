from collections import deque

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    graph[edge].append(node)

for i in range(n + 1):
    graph[i].sort()


def recur_dfs(graph, node):
    print(node, end=' ')

    visited[node] = True
    for edge in graph[node]:
        if not visited[edge]:
            recur_dfs(graph, edge)


recur_dfs(graph, start)

print()


def bfs(graph, start_node):
    q = deque([start_node])

    while q:
        node = q.popleft()

        if not visited[node]:
            print(node, end=' ')
            visited[node] = True
            q.extend(graph[node])


visited = [False] * (n + 1)
bfs(graph, start)
