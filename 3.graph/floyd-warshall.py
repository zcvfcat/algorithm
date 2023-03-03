def floyd_warshall(graph):
    # Initialize distance matrix 
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    
    # Calculate shortest path for each vertex to every other vertex
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist