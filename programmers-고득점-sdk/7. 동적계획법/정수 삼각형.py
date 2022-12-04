def solution(triangle):
    height = len(triangle)

    for h in range(1, height):
        width = h + 1

        for index in range(width):
            if index == 0:
                triangle[h][index] += triangle[h-1][0]
            elif index == width - 1:
                triangle[h][index] += triangle[h-1][-1]
            else:
                triangle[h][index] += max(triangle[h-1][index - 1], triangle[h-1][index])

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30)
