def solution(numbers):
    ans = [-1 for _ in range(len(numbers))]
    stack = []

    for i in range(len(numbers)):
        while stack:
            idx = stack.pop()

            if numbers[idx] < numbers[i]:
                ans[idx] = numbers[i]
            else:
                stack.append(idx)
                break
        stack.append(i)

    return ans
        




print(solution([2, 3, 3, 5]) == [3, 5, 5, -1])
print(solution([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1])
