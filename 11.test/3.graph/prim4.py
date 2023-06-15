from heapq import heapify, heappop, heappush
from math import inf

def prim(edges, start_node,):
    visited = [inf for _ in range(len(edges))]
    visited[start_node] = 1
    
    candidate = edges[start_node]
    heapify(candidate)

    mst = []
    total_cost = 0

    while candidate:
        cost, node, edge = heappop(candidate)
        