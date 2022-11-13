import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

digit_limit = int(input())


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def recur_dfs(number, digit):
    if digit_limit == digit:
        print(number)
        return

    for i in range(1, 10):
        if i % 2 == 0:
            continue

        next_number = number * 10 + i

        if is_prime(next_number):
            recur_dfs(next_number, digit + 1)


recur_dfs(2, 1)
recur_dfs(3, 1)
recur_dfs(5, 1)
recur_dfs(7, 1)
