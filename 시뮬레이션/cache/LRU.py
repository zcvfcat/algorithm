cache_size = 3
reference = [4, 2, 3, 4, 5, 6, 5, 4, 7]

cache = []

for ref in reference:

    if ref not in cache:  # 캐시 미스

        if len(cache) < cache_size:  # 캐시 사이즈
            cache.append(ref)
        else:  # 캐시 가득 찰 경우 빼고 넣음
            cache.pop(0)
            cache.append(ref)

    else:  # 캐시 적중
        cache.pop(cache.index(ref))
        cache.append(ref)
