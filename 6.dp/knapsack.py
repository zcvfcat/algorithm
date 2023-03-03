def knapsack(capacity, weights, profits, items):
    n = len(weights)  
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    
    # 각 무게마다 최대 가치 저장
    for c in range(capacity+1):        
        if weights[0] <= c:
            dp[0][c] = profits[0]
                
    # 1부터 n-1까지 아이템 추가하며 최대 가치 산출    
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            
            # 추가하려는 물건을 담을 수 있는 경우의 최대 가치 구하기
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            
            # 추가하려는 물건을 담을 수 없는 경우 기존 상태 그대로 유지
            profit2 = dp[i-1][c]
            
            # 두 경우 중에서 최대 가치 선택
            dp[i][c] = max(profit1, profit2)
            
    return dp[n-1][capacity]

profits = [1, 6, 10, 16]  
weights = [1, 2, 3, 5]  
capacity = 7  
n = len(profits)  

print(knapsack(capacity, weights, profits, n))      # 출력 : 22