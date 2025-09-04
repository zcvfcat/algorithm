from directions import DIRS_4, move


def simulate_grid_commands(n, m, start, commands):
    """
    격자에서 명령을 따라 이동하는 간단한 시뮬레이터.
    - n, m: 격자 크기 (행, 열)
    - start: 시작 좌표 (r, c)
    - commands: 문자열. 'L' 좌회전, 'R' 우회전, 'F' 전진
    - 반환: 최종 위치 (r, c) 및 마지막 방향 인덱스
    """
    r, c = start
    dir_idx = 0  # 0:상, 1:우, 2:하, 3:좌
    for cmd in commands:
        if cmd == 'L':
            dir_idx = (dir_idx + 3) % 4
        elif cmd == 'R':
            dir_idx = (dir_idx + 1) % 4
        elif cmd == 'F':
            nr, nc = move((r, c), dir_idx, DIRS_4)
            if 0 <= nr < n and 0 <= nc < m:
                r, c = nr, nc
        else:
            raise ValueError("알 수 없는 명령: " + cmd)
    return (r, c), dir_idx


