from heapq import heapify, heappop, heappush
from math import inf

# graph = [[weight, edge]] index = node


def prim(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0

    visited = set()
    mst = []
    node = start_node

    while len(visited) < len(graph):
        visited.add()

        for weight, edge in graph[node]:
            if edge in visited:
                continue

            if weight < distance[edge]:
                distance[edge] = weight

        