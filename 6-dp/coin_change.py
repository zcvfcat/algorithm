def min_coins(coins, amount):
    """
    동전 교환: 최소 동전 개수
    - 반환: 최소 개수(불가능하면 -1)
    - 시간: O(n*amount)
    """
    INF = 10 ** 18
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
    return -1 if dp[amount] >= INF else dp[amount]


def count_ways(coins, amount):
    """
    동전 교환: 경우의 수 (조합, 순서 무시)
    - 반환: 방법 수
    - 시간: O(n*amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


