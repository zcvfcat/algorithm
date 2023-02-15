cache_size = 3
jobs = [4, 2, 3, 4, 5, 6, 5, 4, 7]

cache = []

for job in jobs:
    if job not in cache: # 프로세스 일 경우 캐시 미스율, 페이지 일 경우 페이지 폴트
        if len(cache) < cache_size:
            cache.append(job)
        else:
            cache.pop(0)
            cache.append(job)
    else:
        cache.pop(cache.index(job))
        cache.append(job)