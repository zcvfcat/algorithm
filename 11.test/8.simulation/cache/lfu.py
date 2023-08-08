def lfu(cacheSize, pages):
    pageFaults = 0
    cache = []

    if cacheSize == 0:
        return len(pages)

    for page in pages:

        if page in cache:
            cache.remove(page)
            cache.append(page)
        else:
            pageFaults += 1

            if len(cache) == cacheSize:
                freq = [cache.count(c) for c in cache]
                idx = freq.index(min(freq))
                cache.pop(idx)

            cache.append(page)
    return pageFaults


print(lfu(3, [2, 3, 1, 3, 2, 1, 4, 3]))
