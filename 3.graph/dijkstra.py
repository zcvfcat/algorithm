import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        (dist, current_vertex) = heapq.heappop(pq)
        if dist > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


graph = {
    'A': {'B': 3, 'D': 4},
    'B': {'A': 3, 'C': 1},
    'C': {'B': 1, 'D': 5},
    'D': {'A': 4, 'C': 5}
}

distances = dijkstra(graph, 'A')

print(distances)
# {'A': 0, 'B': 3, 'C': 4, 'D': 4}
