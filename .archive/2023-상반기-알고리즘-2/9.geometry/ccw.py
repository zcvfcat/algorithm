def orientation(p, q, r):
    '''오리엔테이션(3점의 위치관계) 확인'''
    val = (q[1]-p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])
    if val == 0:
        return 0 # 일직선
    elif val > 0:
        return 1 # 반시계 방향
    else: 
        return 2 # 시계 방향

def ccw(points):
    '''CCW 알고리즘'''
    n = len(points)
    points = sorted(points) # 최소의 x값을 찾기 위해서 정렬
    hull = []
    
    # 첫번째와 2~n번째 요소까지 거리를 계산하여 제일 아래 점부터 시계 방향으로 정렬 (제자리)
    l = 0
    for i in range(n):
        if points[i][1] < points[l][1]:
            l = i
    
    # 최소 x 값인 점부터 반시계 방향으로 정렬 (Graham Scan)
    p = l
    while True:
        hull.append(points[p])
        q = (p+1) % n # 다음 점 위치
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
            
    return hull