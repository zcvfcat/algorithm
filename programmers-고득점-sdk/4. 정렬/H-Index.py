def solution(citations):
    citations.sort()

    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0


print(solution([3, 0, 6, 1, 5]) == 3)
