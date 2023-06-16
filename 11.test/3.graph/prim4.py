from heapq import heapify, heappop, heappush


# graph = [[weight, edge]] index = node
def prim(graph, start_node):
    visited = [False for _ in range(len(graph))]
    visited[start_node] = True

    candidate = graph[start_node]
    heapify(candidate)

    total = 0

    while candidate:
        if visited:
            return total

        cost, edge = heappop(candidate)
        
