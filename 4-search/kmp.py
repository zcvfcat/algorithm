def build_lps(pattern):
    """
    KMP의 부분일치 테이블(LPS: Longest Prefix which is also Suffix) 생성.
    lps[i]: 패턴[0..i]에서 접두사이면서 접미사인 최대 길이
    """
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pattern):
    """
    KMP 문자열 검색: text에서 pattern이 등장하는 시작 인덱스들을 반환.
    평균/최악 모두 O(n + m).
    """
    if pattern == "":
        return list(range(len(text) + 1))
    lps = build_lps(pattern)
    res = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                res.append(i - j)
                j = lps[j - 1]
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1
    return res


