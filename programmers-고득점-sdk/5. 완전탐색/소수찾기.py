from itertools import permutations


def is_prime(number):
    if number < 2:
        return False

    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False

    return True


def solution(numbers):
    ans = set()
    for i in range(1, len(numbers) + 1):
        for k in permutations(numbers, i):
            ans.add(int(''.join(k)))

    count = 0
    for e in [*ans]:
        if is_prime(e):
            count += 1

    return count


print(solution("17") == 3)
print(solution("011") == 2)
