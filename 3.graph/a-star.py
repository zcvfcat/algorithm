import heapq


def astar(start_node, goal_node, heuristic_func):
    """
    Implementation of the A* algorithm.
    
    :param start_node: The starting node of the search
    :param goal_node: The goal node to reach
    :param heuristic_func: A function that takes a Node object and returns its heuristic value
    :return: The optimal path from start_node to goal_node, as a list of Nodes
    """
    # Maintain a set of visited nodes
    visited = set()
    
    # PriorityQueue (min-heap) of frontier nodes
    frontier = []
    
    # Initialize the min-heap with (f(n), n) tuple for the start node
    start_cost = 0 + heuristic_func(start_node)
    heapq.heappush(frontier, (start_cost, start_node))
    
    # Initialize the came_from dictionary to reconstruct the final path
    came_from = {start_node: None}
    
    
    while len(frontier) > 0:
        # Pop the node with minimum f(n) value from the PQ
        curr_node = heapq.heappop(frontier)[1]
        
        # If we have reached the goal state, return the optimal path
        if curr_node == goal_node:
            path = [curr_node]
            
            while path[-1] != start_node:
                path.append(came_from[path[-1]])
            
            return list(reversed(path))
        
        # Add current node to the visited set
        visited.add(curr_node)
        
        # Check all neighbours that haven't been visited yet
        for neighbour in curr_node.get_neighbours():
            if neighbour in visited:
                continue
                
            # Compute the cost of getting to the neighbour through the current node
            tentative_g_score = curr_node.g_score + curr_node.get_edge_weight(neighbour)
            tentative_f_score = tentative_g_score + heuristic_func(neighbour)
            
            # Add the neighbour to the frontier PQ if it's not already present, or has a higher priority
            if neighbour not in [x[1] for x in frontier]:
                heapq.heappush(frontier, (tentative_f_score, neighbour))
                
            # If the neighbour is in the frontier PQ and has lower priority, update its priority
            else:
                index = [i for i, x in enumerate(frontier) if x[1] == neighbour][0]
                if tentative_f_score < frontier[index][0]:
                    frontier[index] = (tentative_f_score, neighbour)
                    heapq.heapify(frontier)
            
            # Update the path reconstruction dictionary
            came_from[neighbour] = curr_node
    
    # If we couldn't find a path from start to goal, return None
    return None