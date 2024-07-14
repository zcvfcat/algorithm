def bfs(graph):
    visited = set()
    queue = [(0, [0])]  # Start at node 0 with distance 0

    while queue:
        distance, path = queue.pop(0)

        if path[-1] == len(graph) - 1:
            return distance

        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((distance + 1, path + [neighbor]))

    return -1