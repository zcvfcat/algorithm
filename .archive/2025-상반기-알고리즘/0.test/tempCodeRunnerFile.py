
# Test Case 1: 간단한 그래프
graph1 = [
    [(1, 3), (2, 5)],  # Node 0 connects to Node 1 (cost 3) and Node 2 (cost 5)
    [(0, 3), (2, 1)],  # Node 1 connects to Node 0 (cost 3) and Node 2 (cost 1)
    [(0, 5), (1, 1)]   # Node 2 connects to Node 0 (cost 5) and Node 1 (cost 1)
]
print("Test Case 1:")
pprint(floyd_warshall(graph1))
