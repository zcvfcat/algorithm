import heapq
from math import inf, sqrt


def astar(minimap: list, start_y, start_x, end_y, end_x):
    distances = [[inf for _ in range(len(minimap))] for _ in range(len(minimap[0]))]
    distances[start_y][start_x] = 0
    
    h = []



def heuristic(node, goal):
    y, x = node
    end_y, end_x = goal

    return sqrt((end_y - y) ** 2 + (end_x - x) ** 2)


minimap = [
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, 3, 4, 5]
]
start = (0, 0)
end = (4, 4)
