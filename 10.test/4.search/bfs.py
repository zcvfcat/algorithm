# from collections import deque


# def bfs(graph, start, end):
#     visited = [False for _ in range(len(graph))]
#     q = deque([start])

#     parents = [i for i in range(len(graph))]

#     while q:
#         node = q.popleft()

#         if node == end:
#             break

#         for edge in graph[node]:
#             if visited[edge] is False:
#                 visited[edge] = node
#                 parents[edge] = node
#                 q.append(edge)

#     path = end
#     paths = [path]

#     while parents[path] is not path:
#         paths.append(path)
#         path = parents[node]

#     paths.reverse()

#     return paths
