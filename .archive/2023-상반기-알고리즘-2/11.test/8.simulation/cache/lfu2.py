jobs = []
size = 3
cache = []

for job in jobs:
    if job in cache:
        del cache[cache.index(job)]
        cache.append(job)
    else:
        if len(cache) < size:
            cache.append(job)
        else:
            freq = [cache.count(c) for c in cache]
            idx = freq.index(min(freq))
            cache.pop(idx)