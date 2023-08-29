# 하향식 (메모이제이션)
def fibonacci(n):
    memo = [0, 1]

    for idx in range(2, n):
        memo[idx] = memo[idx - 1] + memo[idx - 2]

    return memo[n]

# 상향식 (재귀)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)