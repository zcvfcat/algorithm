from collections import deque

cache_size = 3
jobs = [4, 2, 3, 4, 5, 6, 5, 4, 7]

cache = deque([])

for job in jobs:
    if job not in cache:
        if len(cache) < cache_size:
            cache.append(job)
        else:
            cache.popleft()
            cache.append(job)
    else:
        del cache[cache.index(job)]
        cache.append(job)

print(cache)