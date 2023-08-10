def sltf(start, requests):
    # 서비스할 요청들을 저장할 변수를 초기화합니다.
    serviced_req = []
    # 이동 거리의 총합을 저장할 변수를 초기화합니다.
    total_distance = 0

    while len(requests) > 0:
        # 현재 헤드 위치에서 가장 가까운 요청을 찾습니다.
        nearest_req = min(requests, key=lambda req: abs(req - start))
        # 가장 가까운 요청을 서비스합니다.
        serviced_req.append(nearest_req)
        total_distance += abs(start - nearest_req)
        # 서비스가 완료된 요청은 요청 리스트에서 제거합니다.
        requests.remove(nearest_req)
        # 서비스한 요청의 위치로 헤드를 이동합니다.
        start = nearest_req

    # 서비스된 요청들과 이동 거리의 총합을 반환합니다.
    return serviced_req, total_distance


# 사용 예시
if __name__ == "__main__":
    start = 50
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    serviced_req, total_distance = sltf(start, requests)
    print("서비스된 요청: ", serviced_req)
    print("이동 거리의 총합: ", total_distance)
