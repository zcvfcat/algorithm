from itertools import combinations


def binomial(n, r):
    return len([*combinations(range(n), r)])


print(binomial(5, 2))
