from collections import deque

def bfs(graph,start,end):
    visited = [-1 for _ in range(len(graph))]

    visited[start] = 0
    q = deque([start])
    
    while q:
        node = q.popleft()

        if node == end:
            return visited[node]
        
        for edge in graph[node]:
            if visited[edge] == -1:
                visited[edge] = visited[node] + 1
                q.append(edge)
    return -1

def dfs(graph, visited, node, end):
    if node == end:
        return visited[node]
    
    for edge in graph[node]:
        if visited[edge] == -1:
            visited[edge] = visited[node] + 1
            result = dfs(graph, visited, edge, end)

            if result != -1:
                return result
    
    return -1

graph = [[3,4],[1,2],[1,4],[2,4],[3]]
visited =[-1 for _ in range(len(graph))]
start = 0
end = 4

result = dfs(graph, visited, start, end)
