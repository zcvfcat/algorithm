# 서로소 집합

def find(parents, vertex):
    if parents[vertex] != vertex:
        parents[vertex] = find(parents, parents[vertex])
    return parents[vertex]


def union(parents, vertex_a, vertex_b):
    vertex_a = find(parents, vertex_a)
    vertex_b = find(parents, vertex_b)

    if vertex_b != vertex_a:
        parents[vertex_b] = vertex_a


parents = [vertex for vertex in range(10)]

union(parents, 1, 4)
union(parents, 5, 6)
union(parents, 1, 6)

groups = set(map(lambda x: find(parents, x), parents))

print(groups)
