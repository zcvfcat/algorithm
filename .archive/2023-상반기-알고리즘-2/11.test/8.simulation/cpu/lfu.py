def lfu(cache_size, pages):
    page_fault = 0
    cache = []

    if cache_size ==0:
        return len(pages) # cache가 없음
    
    for page in pages:

        if page in cache:
            cache.remove(page)
            cache.append(page)
        else:
            page_fault += 1

            if len(cache) == cache_size:
                freq = [cache.count(c) for c in cache]
                idx = freq.index(min(freq))
                cache.pop(idx)
            
            cache.append(page)
    
    return page_fault

cache_size = 3
jobs = [2, 3, 1, 3, 2, 1, 4, 3]

print(lfu(cache_size, jobs))