from collections import deque

def topology(graph):
    in_degree = [0 for _ in len(graph)]

    for edges in graph:
        for edge in edges:
            in_degree[edge] += 1
    
    q = deque()

    for node, status in enumerate(in_degree):
        if status ==0:
            q.append(node)
    
    sorted_array = []

    while q:
        node = q.popleft()
        sorted_array.append(node)

        for edge in graph[node]:
            in_degree[edge] -= 1

            if in_degree[edge] == 0:
                q.append(edge)
    
    return sorted_array