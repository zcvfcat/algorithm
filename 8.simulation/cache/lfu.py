def lfu(cacheSize, pages):
    pageFaults = 0
    cache = []
    
    # 캐시의 크기가 0인 경우, 페이지 결함 수 리턴
    if cacheSize == 0:
        return len(pages)
    
    for page in pages:
        # 캐시에 페이지가 이미 있는 경우
        if page in cache:
            cache.remove(page) # 해당 페이지 삭제 후
            cache.append(page) # 맨 뒤에 추가
        else:
            pageFaults += 1
            # 캐시가 꽉 찬 경우, 가장 frequency 값이 작은 것 삭제
            if len(cache) == cacheSize:
                freq = [cache.count(c) for c in cache]
                idx = freq.index(min(freq))
                cache.pop(idx)
            cache.append(page)

    return pageFaults

print(lfu(3, [2,3,1,3,2,1,4,3]))