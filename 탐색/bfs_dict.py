from collections import deque

graph = {
    1: (2, 3, 8),
    2: (1, 6, 8),
    3: (1, 4, 5),
    4: (3,),
    5: (3,),
    6: (2, 7),
    7: (6,),
    8: (1, 2),
}


node_length = len(graph.keys())

visited = {}
for key in graph.keys():
    visited[key] = False


def bfs(start_node):
    q = deque([start_node])
    visited[start_node] = True
    searched = []

    while q:
        node = q.popleft()
        searched.append(node)

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)

    return searched


print(bfs(1))
