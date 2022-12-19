from collections import deque

jobs = [(0, 3), (1, 9), (2, 6)]


def RR(jobs):
    jobs.sort()
    q = deque(jobs)
    request, process = q.popleft()

    completed = request + process

    while q:
        request, process = q.popleft()

        if completed < request:
            completed = request

        completed = completed + process

    return completed


print(RR(jobs))
