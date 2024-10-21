from heap import heappush, heappop
from math import inf


def dijkstra(graph, start):
    visited = set()
    distances = {vertex: inf for vertex in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(queue, (distance, neighbor))

    return distances