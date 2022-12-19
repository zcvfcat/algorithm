from collections import Counter

patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
]


def solution(answers):
    solved = [0 for _ in range(len(patterns))]

    for index, pattern in enumerate(patterns):
        for i in range(len(answers)):
            if answers[i] == pattern[i % len(pattern)]:
                solved[index] += 1

    max_score = max(solved)

    ans = []
    for i in range(len(solved)):
        if max_score == solved[i]:
            ans.append(i + 1)

    return ans


print(solution([1, 2, 3, 4, 5]) == [1])
print(solution([1, 3, 2, 4, 2]) == [1, 2, 3])
