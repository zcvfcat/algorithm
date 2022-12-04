def solution(money):
    n = len(money)
    dp = [
        [money[0], money[0]],
        [0, money[1]]
    ]

    for i in range(2, n-1):
        dp[0].append(max(dp[0][i-1], dp[0][i-2] + money[i]))
        dp[1].append(max(dp[1][i-1], dp[1][i-2] + money[i]))

    dp[0].append(dp[0][-1])
    dp[1].append(dp[1][-2] + money[-1])

    return max(dp[0][-1], dp[1][-1])


print(solution([1, 2, 3, 1]) == 4)
