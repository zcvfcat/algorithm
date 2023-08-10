def cscan(start, requests, end):
    service_req = []
    total_distance = abs(start - requests[0])

    left_req = [req for req in requests if req < start]
    right_req = [req for req in requests if req >= start]

    for req in right_req:
        service_req.append(req)
        total_distance += abs(start - req)
        start = req
    
    if start < end:
        total_distance += abs(start - end)
        start = end
    
    total_distance += abs(start - 0)
    start = 0

    for req in left_req:
        service_req.append(req)
        total_distance += abs(start - req)
        start = req
    
    return service_req, total_distance

start = 50
end = 199
requests = [98, 183, 37, 122, 14, 124, 65, 67]
serviced_req, total_distance = cscan(start, requests, end)
print("서비스된 요청: ", serviced_req)
print("이동 거리의 총합: ", total_distance)