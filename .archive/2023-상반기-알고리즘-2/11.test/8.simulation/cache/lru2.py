from collections import deque

jobs = []
size = 3
cache = deque([])

for job in jobs:
    if job in cache:
        del cache[cache.index(job)]
        cache.append(job)
    else:
        if len(cache) < size:
            cache.append(job)
        else:
            cache.popleft()
            cache.append(job)