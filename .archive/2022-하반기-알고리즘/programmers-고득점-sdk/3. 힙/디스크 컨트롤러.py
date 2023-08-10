import heapq


def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]

    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))

        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += (time - start)

        else:
            time += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))               # 9
print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
print(solution([[0, 10]]))                              # 10
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74
