
def prefix(s):
    n = len(s)
    pi = [0] * n  # pi 배열 초기화
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:  # 일치하지 않으면 j를 이전 값으로 갱신
            j = pi[j-1]
        if s[i] == s[j]:  # 일치하면 j를 증가시키고 pi 배열 갱신
            j += 1
            pi[i] = j

    return pi


s = "ababaca"
pi = prefix(s)
print(pi)  # [0, 0, 1, 2, 3, 0, 1]
