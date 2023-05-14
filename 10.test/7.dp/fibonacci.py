def fibo(n, memo):
    if n == 0 or n == 1:
        return n
    
    if memo[n] != None:
        return memo[n]
    
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)

    return memo[n]

n = 10
memo = [None] * (n + 1)
print(fibo(n, memo))