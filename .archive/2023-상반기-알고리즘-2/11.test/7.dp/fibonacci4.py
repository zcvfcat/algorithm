def fibo(n):
    if n < 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo2(n):
    memo = [0 for _ in range(len(n + 1))]
    memo[0], memo[1] = 1, 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    
    return memo[n]