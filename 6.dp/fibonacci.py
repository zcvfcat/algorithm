def fibonacci(n):
    memo = [0, 1]

    for idx in range(2, n + 1):
        memo.append(memo[idx - 1] + memo[idx -2])

    return memo[n]

def fibonacci_recur(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)