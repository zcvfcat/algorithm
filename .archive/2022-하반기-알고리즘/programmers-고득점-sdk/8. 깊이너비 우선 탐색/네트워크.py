from collections import Counter


def solution(n, computers):
    groups = [i for i in range(n)]

    def find(node):
        if groups[node] != node:
            groups[node] = find(groups[node])
        return groups[node]

    def union(node_a, node_b):
        node_a = find(node_a)
        node_b = find(node_b)

        if node_a <= node_b:
            groups[node_b] = node_a
        else:
            groups[node_a] = node_b

    for node in range(n):
        for edge in range(n):
            if node != edge:
                if computers[node][edge] == 1:
                    union(node, edge)

    counter = {}
    for group in groups:
        node = find(group)

        if node in counter:
            counter[node] += 1
        else:
            counter[node] = 1

    return len(counter)


print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)
