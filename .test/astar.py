import heapq # this is astar????
from math import inf


def astar(edges, nodes, end):
    dist = [inf for _ in range(len(nodes))]
    dist[0] = 0
    q = []

    heapq.heappush(q, [0, [0]])

    while q:
        _, paths = heapq.heappop(q)
        last = paths[-1]

        if last == end:
            return paths

        for edge, weight in edges[last]:
            cost = dist[last] + weight

            if dist[edge] > cost:
                dist[edge] = cost

                heapq.heappush(q, [cost + nodes[edge], paths + [edge]])
    return []


nodes = [10, 14, 10, 10, 9, 9, 5, 0, 9, 8, 6, 4, 7, 3]

edges = [
    [[4, 1], [5, 1]],
    [[2, 12], [3, 4], [4, 15]],
    [[1, 12], [9, 2], [11, 6]],
    [[1, 4], [5, 3], [8, 3]],
    [[1, 15], [0, 1], [6, 6]],
    [[0, 1], [3, 3], [6, 4]],
    [[4, 6], [5, 4], [10, 1]],
    [[11, 4], [13, 5]],
    [[3, 3], [9, 1], [10, 5]],
    [[2, 2], [8, 1], [12, 1]],
    [[6, 1], [8, 5], [13, 3]],
    [[2, 6], [7, 4], [12, 5]],
    [[9, 1], [11, 5], [13, 6]],
    [[7, 5], [10, 3], [12, 6]]
]
print(astar(edges, nodes, 7))
