graph = [[1,2,3],[2,3],[1,3],[0]]
visited = [0 for _ in range(len(graph))]

def dfs(graph, node):
    for edge in graph[node]:
        if visited[edge] == 0:
            visited[edge] = visited[node] + 1
            dfs(graph,node)