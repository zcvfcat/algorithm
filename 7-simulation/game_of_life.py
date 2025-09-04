def next_state(board):
    """
    Conway's Game of Life의 다음 세대 보드 상태를 계산합니다.
    - board: 0(죽음)/1(생존) 2D 리스트
    - 반환: 같은 크기의 다음 세대 보드
    규칙:
      - 살아있는 셀은 이웃(8방향) 생존 수가 2 또는 3이면 생존, 아니면 사망
      - 죽은 셀은 이웃 생존 수가 정확히 3이면 부활
    """
    if not board or not board[0]:
        return board
    n, m = len(board), len(board[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    res = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            live = 0
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m:
                    live += board[nr][nc]
            if board[r][c] == 1:
                res[r][c] = 1 if live in (2,3) else 0
            else:
                res[r][c] = 1 if live == 3 else 0
    return res


