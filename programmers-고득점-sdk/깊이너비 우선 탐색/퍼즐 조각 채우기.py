step = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_boundary(y, x):
    global height, width
    return y < height and y >= 0 and x < width and x >= 0


def rotate90(input):
    global height, width
    output = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            output[y][width - 1 - x] = input[y][x]

    return output


def dfs(y, x, game_board, space=[]):
    space.append((y, x))

    for dy, dx in step:
        ny = y + dy
        nx = x + dx

        if in_boundary(ny, nx) and game_board[ny][nx] == 0:
            game_board[ny][nx] = 2
            space = space + dfs(ny, nx, game_board, space)

    return space


def solution(game_board, table):
    global height, width
    height = len(game_board)
    width = len(game_board[0])

    spaces = []

    for row in game_board:
        print(row)

    for y in range(height):
        for x in range(width):
            if game_board[y][x] == 0:
                game_board[y][x] = 2
                space = dfs(y, x, game_board)
                spaces.append(space)
    print()

    for row in game_board:
        print(row)
    print()
    for row in spaces:
        print(row)


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
      [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]) == 14)
# print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]) == 0)
