
def solution(n, computers):
    groups = [i for i in range(n)]

    def find(node):
        if node != groups[node]:
            groups[node] = find(groups[node])
        return groups[node]

    def union(node_a, node_b):
        node_a = find(node_a)
        node_b = find(node_b)

        if node_a != node_b:
            groups[node_b] = node_a

    for node, edges in enumerate(computers):
        for edge, value in enumerate(edges):
            if node != edge and value == 1:
                union(node, edge)
    
    return len(set(map(lambda x: find(x),groups)))

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
