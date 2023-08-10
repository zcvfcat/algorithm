def solution(array, commands):
    ans = []
    for i, j, k in commands:
        target = array[i - 1: j]
        target.sort()
        ans.append(target[k - 1])
    return ans


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3])
