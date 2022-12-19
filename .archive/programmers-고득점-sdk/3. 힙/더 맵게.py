import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K:
        next_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, next_scoville)
        count += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return count


print(solution([1, 2, 3, 9, 10, 12], 7) == 2)
