def fibonacci(num: int):
    if num == 0:
        return 0
    
    if num == 1 or num == 2:
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)

def memo_fibonacci(num: int):
    if num == 0:
        return 0
    
    if num == 1 or num == 2:
        return 1
    
    memo = [0, 1]

    for i in range(3, num + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    
    return memo[num]