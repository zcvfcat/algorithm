def solution(brown, yellow):
    area = brown + yellow

    for width in range(int(area/2) + 1, -1, -1):
        if area % width != 0:
            continue

        height = area / width

        if (width - 2) * (height - 2) == yellow:
            return [width, height]


print(solution(10, 2) == [4, 3])
print(solution(8, 1) == [3, 3])
print(solution(24, 24) == [8, 6])
