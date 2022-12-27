string = 'babad'


def longestPalaindrome(s: str) -> str:
    if len(s) < 2 or s == s[:: -1]:
        return s

    def expend(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

    ans = ''
    for i in range(len(s) - 1):
        ans = max(ans, expend(i, i + 1), expend(i, i + 2), key=len)

    return ans


print(longestPalaindrome(string))
