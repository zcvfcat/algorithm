import heapq
jobs = [(0, 3), (1, 9), (2, 6)]


def SRTF(jobs):
    # 입력 받은 리스트를 힙 데이터 구조로 변환
    heap = []
    for job in jobs:
        heapq.heappush(heap, job)

    t = 0
    result = []
    # 힙 데이터 구조가 빌 때까지 반복
    while heap:
        job = heapq.heappop(heap)
        t += job[1]
        result.append((job[0], t))
    return result


result = SRTF(jobs)
print(result)
