from heapq import heapify, heappop, heappush

visited = []


def prim(graph, start_node):
    visited[start_node] = 1
    candidate = graph[start_node]
    heapify(candidate)

    mst = []
    total_weight = 0

    while candidate:
        weight, node, edge = heappop(candidate)

        if visited[edge] == 0:
            mst.append((node, edge))
            total_weight += weight

            for next_weight, current_edge, next_edge in graph[edge]:
                if visited[next_edge] == 0:
                    heappush(candidate, next_edge)

    return total_weight
