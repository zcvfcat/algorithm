# 방향을 정의: 북(0), 동(1), 남(2), 서(3) 순서
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_left(direction):
    # 현재 방향에서 왼쪽으로 회전 (반시계 방향으로 90도)
    return (direction - 1) % 4

def turn_right(direction):
    # 현재 방향에서 오른쪽으로 회전 (시계 방향으로 90도)
    return (direction + 1) % 4

def move(pos, direction):
    # 현재 위치에서 방향에 따라 이동
    return (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1])

def is_valid(maze, pos):
    # 미로 내에서 유효한 좌표인지 확인
    return 0 <= pos[0] < len(maze) and 0 <= pos[1] < len(maze[0]) and maze[pos[0]][pos[1]] == 0

def find_exit_with_left_hand_rule(maze, start, exit):
    # 시작 위치와 방향 (처음엔 동쪽(오른쪽) 방향으로 시작)
    position = start
    direction = 1  # 동쪽

    path = [position]  # 경로 기록
    
    while position != exit:
        # 왼쪽 방향으로 회전한 후 이동할 수 있는지 확인
        left_direction = turn_left(direction)
        left_pos = move(position, left_direction)

        if is_valid(maze, left_pos):
            # 왼쪽이 비어 있으면, 왼쪽으로 회전하고 이동
            direction = left_direction
            position = left_pos
        elif is_valid(maze, move(position, direction)):
            # 앞쪽이 비어 있으면, 현재 방향으로 이동
            position = move(position, direction)
        else:
            # 그렇지 않으면, 오른쪽으로 회전
            direction = turn_right(direction)
        
        path.append(position)

    return path

# 미로 (0: 길, 1: 벽)
maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# 시작점과 출구
start = (1, 1)
exit = (4, 4)

# 좌수법을 사용한 경로 찾기
path = find_exit_with_left_hand_rule(maze, start, exit)

print("찾은 경로:", path)