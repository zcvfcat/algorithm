def solution(pocket_mons):
    return min(len(pocket_mons)/2, len(set(pocket_mons)))


print(solution([3, 1, 2, 3]) == 2)
print(solution([3, 3, 3, 2, 2, 4]) == 3)
print(solution([3, 3, 3, 2, 2, 2]) == 2)
