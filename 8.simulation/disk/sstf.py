def sstf(start, requests):
    # 요청 리스트를 현재 헤드 위치에서부터 거리를 계산하여 정렬합니다.
    sorted_req = sorted(requests, key=lambda x: abs(x - start))

    # 서비스된 요청과 거리의 총합을 저장할 변수를 초기화합니다.
    serviced_req = []
    total_distance = 0

    # 요청 리스트가 빌 때까지 반복합니다.
    while sorted_req:
        # 현재 헤드 위치에서 가장 가까운 요청을 선택합니다.
        next_req = sorted_req.pop(0)

        # 선택된 요청까지의 거리를 계산하고 서비스합니다.
        distance = abs(start - next_req)
        total_distance += distance
        serviced_req.append(next_req)

        # 다음 요청을 서비스하기 위해 현재 헤드 위치를 업데이트합니다.
        start = next_req

    # 서비스된 요청과 거리의 총합을 반환합니다.
    return serviced_req, total_distance


start = 50
requests = [82, 170, 43, ]
print(sstf(start, requests))
