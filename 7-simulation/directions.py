DIRS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌
DIRS_8 = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1),
]


def move(pos, dir_idx, dirs=DIRS_4):
    """
    현재 위치 pos = (r, c)에서 dirs[dir_idx] 방향으로 한 칸 이동한 좌표 반환
    """
    r, c = pos
    dr, dc = dirs[dir_idx]
    return r + dr, c + dc


