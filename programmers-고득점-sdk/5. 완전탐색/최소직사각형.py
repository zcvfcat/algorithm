def solution(sizes):
    max_height = 0
    max_width = 0

    for size in sizes:
        height, width = sorted(size)

        max_height = max(max_height, height)
        max_width = max(max_width, width)

    return max_height * max_width


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]) == 120)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]) == 133)
