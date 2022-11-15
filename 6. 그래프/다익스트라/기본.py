INF = float('inf')
width = 5
start = 1

graph = [
  [],
  [(2,1),(3,3)],
  [(3,1),(4,5)],
  [(4,2)],
  [],
  [(1,1)]
]

distance = [INF] * (l + 1)
visited = [False] * (l + 1)

def get_smallest_distance():
  min_weight = INF
  min_edge = 0
  
  for edge in range(1, width + 1):
    if distance[edge] < min_weight and not visited[edge]:
      min_weight = distance[edge]
      min_edge = edge

  return min_edge


def dijkstra(start_node):
  distance[start_node] = 0
  visited[start_node] = True

  for edge, weight in graph[start_node]:
    distance[edge] = weight

  for _ in range(width - 1):
    min_edge = get_smallest_distance()
    visited[min_edge] = True

    for next_edge, next_weight in graph[min_edge]:
      if distance[min_edge] + next_weight < distance[next_edge]:
        distance[next_weight] = distance[min_edge] + next_weight

dijkstra(start)
print(distance)
