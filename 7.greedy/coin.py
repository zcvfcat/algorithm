def coin_change(coins, amount):
    if amount == 0:
        return 0
    
    # 초기값 설정
    num_coins = float('inf')
    
    # 모든 동전 탐색
    for coin in coins:
        # 현재 가능한 상황인 경우에 대해서만 처리
        if amount - coin >= 0:
            current_num_coins = coin_change(coins, amount-coin)
            # 현재 구한 동전 개수가 초기값보다 작을 경우 초기값 갱신
            if current_num_coins < num_coins:
                num_coins = current_num_coins + 1
    
    return num_coins