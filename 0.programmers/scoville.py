from heapq import heappop, heappush, heapify


def s(scoville, K):
    heapify(scoville)
    count = 0

    while scoville[0] < K:
        next_scoville = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, next_scoville)
        count += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return count
