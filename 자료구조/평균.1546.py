n = int(input())
numbers = list(map(int, input().split(' ')))
max_number = max(numbers)
print((sum(numbers) * 100 / max_number)/n)
