def recur_fibonacci(n):
    if n == 0 :
        return 0

    if n <= 2:
        return 1
    
    return recur_fibonacci(n - 2) + recur_fibonacci(n - 1)

def fibonacci(n):
    memo = [0, 1]

    for i in range(1, n):
        memo.append(memo[i] + memo[i - 1])
    
    return memo[n]

print(fibonacci(3))