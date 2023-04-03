def c_look(start, requests):
    total_dist = 0
    service_req = []

    left_req = [req for req in requests if req < start]
    right_req = [req for req in requests if req >= start]

    for req in sorted(right_req):
        service_req.append(req)
        total_dist += abs(start- req)
        start = req
    
    for req in sorted(left_req, reverse=True):
        service_req.append(req)
        total_dist += abs(start - req)
        start = req
    
    return service_req, total_dist

start = 50
requests = [98, 183, 37, 122, 14, 124, 65, 67]
serviced_req, total_distance = c_look(start, requests)
print("서비스된 요청: ", serviced_req)
print("이동 거리의 총합: ", total_distance)