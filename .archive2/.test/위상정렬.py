# degree 가 낮은 순으로 정렬하기

from collections import deque

graph = [
    [],
    [2, 5],
    [3, 6],
    [4],
    [7],
    [6],
    [4],
    [],
]

degrees = [0 for _ in range(len(graph))]

# degree 넣기
for node in range(len(graph)):
    for edge in graph[node]:
        degrees[edge] += 1

# 0을 제외한 degree 중에 최소값 큐에 저장
q = deque()
path = []
for node, degree in enumerate(degrees):
    if node is 0:
        continue

    if degree is 0:
        q.append(node)
        path.append(node)

while q:
    node = q.popleft()

    for edge in graph[node]:
        degrees[edge] -= 1

        if degrees[edge] is 0:
            q.append(edge)
            path.append(edge)

print(degrees)
print(path)

