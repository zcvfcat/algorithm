# G cost = distance from staring node
# H cost = distance from end node  -> heuristic(한국어로 체험)
# F cost = G cost + H cost
# start ---- mid --------- end
# start ---- mid = G
#            mid --------- end = H
# start ------------------ end = F
import sys
import heapq
INF = sys.maxsize

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

vertical_weight, horizon_weight, diagonal_weight = 10, 10, 14  # 피타고라스 정리
step = [
    (1, 0, vertical_weight), (-1, 0, vertical_weight),
    (0, 1, horizon_weight), (0, -1, horizon_weight),
    (1, 1, diagonal_weight), (-1, -1, diagonal_weight),
    (1, -1, diagonal_weight), (1, -1, diagonal_weight),
]

start = (0, 0)
end = (7, 6)

height = len(maze)
width = len(maze[0])


def in_boundary(y, x):
    global height, width

    return 0 <= y < height and 0 <= x < width


class Node:
    def __init__(self, parent=None, position=None) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other: object) -> bool:
        return self.position == other.position


def heuristic(node, goal, d=1, d2=2 ** 0.5):
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])

    return d * (dy + dx) + (d2 - 2*d) * min(dy, dx)


def a_star(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list:

        current_node = open_list[0]
        current_idx = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_idx = index

        open_list.pop(current_idx)
        closed_list.append(current_idx)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []

        for dy, dx, weight in step:
            ny = current_node.position[0] + dy
            nx = current_node.position[1] + dx

            if in_boundary(ny, nx) and maze[ny][nx] == 0:
                next_node = Node(current_node, (ny, nx))
                children.append(next_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.f

            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            open_list.append(child)


path = a_star(maze, start, end)
print(path)
