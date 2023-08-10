import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for start_node in range(m):
    node, edge = map(int, input().split(' '))
    graph[node].append(edge)
    graph[edge].append(node)


def recur_dfs(graph: list, node: int):
    visited[node] = True
    for edge in graph[node]:
        if not visited[edge]:
            recur_dfs(graph, edge)


count = 0

for start_node in range(1, n + 1):
    if visited[start_node] == False:
        count += 1
        recur_dfs(graph, start_node)

print(count)
