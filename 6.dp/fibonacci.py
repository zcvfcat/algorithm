def fibonacci(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n] != None:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


n = 10
memo = [None] * (n+1)
print(fibonacci(n, memo))
