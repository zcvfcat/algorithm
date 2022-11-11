# 10 1 5 2 3
# 1 5 2 3 10
# 1 2 3 5 10

# 9 7 5 3 1
# 7 3 5 1 9
# 3 5 1 7 9
# 3 1 5 7 9
# 1 3 5 7 9

# 어렵네...

n = int(input())
array = []

for i in range(n):
    array.append((int(input()), i))

sorted_array = sorted(array)

ans = 0

for i in range(n):
    ans = max(ans, sorted_array[i][1] - i + 1)

print(ans)
