def knapsack_01(weights, values, capacity):
    """
    0/1 배낭 문제 (가치 최대화)
    - 입력: weights[i], values[i], capacity
    - 반환: 최대 가치 (정수)
    - 시간: O(n*W), 공간: O(W)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for c in range(capacity, w - 1, -1):
            cand = dp[c - w] + v
            if cand > dp[c]:
                dp[c] = cand
    return dp[capacity]


