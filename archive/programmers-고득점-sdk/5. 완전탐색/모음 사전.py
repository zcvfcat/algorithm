
def solution(word):
    pivot = 'AEIOU'
    ans = 0
    count = 0

    def dfs(w):
        nonlocal count
        nonlocal ans

        if len(w) > 5:
            return

        if word == w:
            ans = count
            return

        count += 1

        for k in pivot:
            dfs(w + k)

    dfs('')

    return ans


print(solution("AAAAE") == 6)
print(solution("AAAE") == 10)
print(solution("I") == 1563)
print(solution("EIO") == 1189)
