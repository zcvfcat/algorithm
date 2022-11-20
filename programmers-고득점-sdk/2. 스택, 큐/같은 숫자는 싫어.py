def solution(array):
    ans = []

    for k, v in enumerate(array):
        if k == 0:
            ans.append(v)
            continue

        if array[k - 1] == v:
            continue
        ans.append(v)

    return ans


print(solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1])
print(solution([4, 4, 4, 3, 3]) == [4, 3])
