def rabin_karp(text, pattern, base=257, mod=1000000007):
    """
    Rabin-Karp 문자열 검색: 롤링 해시로 pattern의 등장 위치를 찾습니다.
    해시 충돌 시 직접 비교로 확인합니다.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n + 1))
    if m > n:
        return []

    power = 1
    for _ in range(m - 1):
        power = (power * base) % mod

    pat_hash = 0
    win_hash = 0
    for i in range(m):
        pat_hash = (pat_hash * base + ord(pattern[i])) % mod
        win_hash = (win_hash * base + ord(text[i])) % mod

    result = []
    for i in range(n - m + 1):
        if pat_hash == win_hash:
            if text[i : i + m] == pattern:
                result.append(i)
        if i < n - m:
            win_hash = (
                (win_hash - ord(text[i]) * power) * base + ord(text[i + 1 + m - 1])
            ) % mod
            if win_hash < 0:
                win_hash += mod
    return result


