from itertools import permutations


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    lst = []
    for l in range(1, len(numbers)):
        k = [*map(lambda x: ''.join(x), permutations(numbers, l))]
        lst.extend(k)

    count = 0
    print(lst)
    for k in set(map(lambda k: int(k), lst)):
        if is_prime(k):
            count += 1
    return count


print(solution("011"))
