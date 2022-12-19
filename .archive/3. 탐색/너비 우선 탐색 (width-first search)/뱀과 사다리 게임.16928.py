from collections import deque
n, m = map(int, input().split())
finish = 100
sadari_edges = []
bam_edges = []
visited = [False] * (finish + 1)
counts = [0] * (finish + 1)

for _ in range(n):
    start, end = map(int, input().split())
    sadari_edges.append([start, end])

for _ in range(m):
    start, end = map(int, input().split())
    bam_edges.append([start, end])


q = deque([1])

while q:
    node = q.popleft()
    visited[node] = True

    if node == finish:
        break

    for scalar in range(1, 7):
        edge = node + scalar

        if edge > finish or edge <= 0 or visited[edge] == True:
            continue

        for start_node, end_node in sadari_edges:
            if start_node == edge:
                edge = end_node

        for start_node, end_node in bam_edges:
            if start_node == edge:
                edge = end_node

        if visited[edge] == False:
            q.append(edge)
            counts[edge] += 1

print(counts)
