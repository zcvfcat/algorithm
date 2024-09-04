def rotate_90_degrees(matrix):
    # 1. 전치 행렬(transpose)을 구한다.
    transposed_matrix = [list(row) for row in zip(*matrix)]

    # 2. 전치된 배열의 각 행을 역순으로 정렬하여 90도 회전한 배열을 구한다.
    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix


# 예시 맵 (2D 배열)
map_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 90도 회전
rotated_map = rotate_90_degrees(map_matrix)

for row in rotated_map:
    print(row)

def rotate_sub_matrix(matrix, start_row, start_col, size):
    # 1. 회전할 서브 매트릭스를 추출한다.
    sub_matrix = [row[start_col:start_col+size] for row in matrix[start_row:start_row+size]]
    
    # 2. 서브 매트릭스를 90도 회전한다.
    transposed_matrix = [list(row) for row in zip(*sub_matrix)]
    rotated_sub_matrix = [row[::-1] for row in transposed_matrix]
    
    # 3. 회전한 서브 매트릭스를 다시 원래 매트릭스에 반영한다.
    for i in range(size):
        matrix[start_row + i][start_col:start_col+size] = rotated_sub_matrix[i]
    
    return matrix

# 예시 맵 (2D 배열)
map_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 좌표 (1,1)부터 2x2 영역을 회전 (즉, 6, 7, 10, 11 부분)
start_row, start_col, size = 1, 1, 2

# 특정 영역 회전
rotated_map = rotate_sub_matrix(map_matrix, start_row, start_col, size)

for row in rotated_map:
    print(row)