# 선택 정렬

def solution(prices):
    ans = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        length = len(prices) - i - 1

        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                length = j - i
                break

        ans[i] = length

    return ans


print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
