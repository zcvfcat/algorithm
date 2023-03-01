"""
(n, r) = n! / (r! * (n-r)!)
이항계수
"""


def binomial(n, r):
    d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(0, n + 1):
        d[i][0] = 1
        d[i][i] = 1
        d[i][1] = i

    for y in range(2, n + 1):  # O(n)
        for x in range(1, i):  # O(n)
            d[y][x] = d[y - 1][x] + d[y - 1][x - 1]

    return d[n][r]


print(binomial(5, 2))
