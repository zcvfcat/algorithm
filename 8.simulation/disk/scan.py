def scan(start, requests):
    # 서비스할 요청들을 저장할 변수를 초기화합니다.
    serviced_req = []
    # SCAN 알고리즘은 요청이 없는 방향으로 이동할 때도 이동 거리를 더해주어야 합니다.
    total_distance = abs(start - requests[0])

    # 요청 리스트를 현재 헤드 위치에서 왼쪽과 오른쪽으로 분리합니다.
    left_req = [req for req in requests if req < start]
    right_req = [req for req in requests if req >= start]

    # 왼쪽 요청 리스트와 오른쪽 요청 리스트를 각각 정렬합니다.
    left_req.sort(reverse=True)
    right_req.sort()

    # 오른쪽으로 이동하면서 요청을 서비스합니다.
    for req in right_req:
        serviced_req.append(req)
        total_distance += abs(start - req)
        start = req

    # 가장 끝까지 이동한 후에 다시 방향을 바꿉니다.
    total_distance += abs(start - max(left_req + right_req))
    start = max(left_req + right_req)

    # 왼쪽으로 이동하면서 요청을 서비스합니다.
    for req in left_req:
        serviced_req.append(req)
        total_distance += abs(start - req)
        start = req

    # 서비스된 요청들과 이동 거리의 총합을 반환합니다.
    return serviced_req, total_distance


# 사용 예시
if __name__ == "__main__":
    start = 50
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    serviced_req, total_distance = scan(start, requests)
    print("서비스된 요청: ", serviced_req)
    print("이동 거리의 총합: ", total_distance)
