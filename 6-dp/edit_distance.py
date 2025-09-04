def edit_distance(a, b):
    """
    편집 거리(Levenshtein): 삽입/삭제/교체 최소 횟수
    - 시간/공간: O(n*m)
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        ai = a[i - 1]
        row = dp[i]
        prev_row = dp[i - 1]
        for j in range(1, m + 1):
            cost = 0 if ai == b[j - 1] else 1
            row[j] = min(
                prev_row[j] + 1,      # 삭제
                row[j - 1] + 1,        # 삽입
                prev_row[j - 1] + cost # 교체
            )
    return dp[n][m]


