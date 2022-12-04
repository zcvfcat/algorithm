def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        deleted_stones = 0  # 제거한 돌을 카운트하기 위한 변수
        pre_stone = 0  # 기준이 되는 돌

        for rock in rocks:
            if rock - pre_stone < mid:
                deleted_stones += 1
            else:
                pre_stone = rock

            if deleted_stones > n:
                break

        if deleted_stones > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer


print(solution(25,	[2, 14, 11, 21, 17], 2) == 4)
