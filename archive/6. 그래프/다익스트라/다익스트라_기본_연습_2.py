import sys

width = 5
start_node = 1

graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = [sys.maxsize] * (width + 1)
visited = [False] * (width + 1)


def get_smallest_distance():
    min_weight = sys.maxsize
    min_edge = 0
