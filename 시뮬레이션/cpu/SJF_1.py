import heapq

jobs = [(0, 3), (1, 9), (2, 6)]


def SJF(jobs: list):
    jobs.sort(reversed=True)

    now = 0 
    count = len(jobs)
    q = []

    ans = 0

    while jobs or q:
        
