from heapq import heappush, heappop

def prim(graph, start_node):
    visited = [False for _ in range(len(graph))]
    visited[start_node] = 0

    mst, q = [], []

    for edge, cost in graph[start_node]:
        heappush(q, (cost, start_node, edge))

    while q:
        cost, node, edge = heappop(q)

        if visited[edge] == True:
            continue
            
        visited[edge] = True
        mst.append((node, edge, cost))

        for next_edge, weight in graph[edge]:
            if not visited[edge]:
                heappush(q, (weight, edge, next_edge))
    
    return mst
