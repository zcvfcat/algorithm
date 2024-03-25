def fibonacci(n):
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n):
    if n == 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    
    memo = [0, 1]

    for i in range(3, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    
    return memo[n]