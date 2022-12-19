# 아우.. 모르겠누;;
import heapq

# start, time
jobs = [(0, 3), (1, 9), (2, 6)]


def SJF(jobs):
    jobs.sort(reverse=True)

    now = 0
    count = len(jobs)
    q = []

    ans = 0

    while jobs or q:

        while jobs and (request := jobs[-1][0]) <= now:
            process = jobs[-1][1]
            heapq.heappush(q, (process, request))
            jobs.pop()

        if q:
            process, request = heapq.heappop(q)
            ans += process + now - request
            now += process
        else:
            now += 1

    return ans // count


print(SJF(jobs))
