def fractional_knapsack(items, max_weight):
    # 물건 가치 대 무게 비율을 계산하여 내림차순으로 정렬
    items = sorted(items, key=lambda item: item[1] / item[0], reverse=True)

    # 최대 가치 초기화
    max_value = 0

    # 배낭에 넣은 무게 초기화
    current_weight = 0

    # 물건들을 하나씩 검사하여 최대 가치를 찾음
    for item in items:
        # 물건의 무게가 남은 배낭의 무게보다 작거나 같은 경우, 물건을 배낭에 넣음
        if current_weight + item[0] <= max_weight:
            current_weight += item[0]
            max_value += item[1]
        # 물건의 무게가 남은 배낭의 무게보다 큰 경우, 일부분만 넣음
        else:
            remain_weight = max_weight - current_weight
            max_value += remain_weight * (item[1] / item[0])
            break

    # 최대 가치 반환
    return max_value
