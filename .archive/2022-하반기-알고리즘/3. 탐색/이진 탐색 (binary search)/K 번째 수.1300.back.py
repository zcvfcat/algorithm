n = int(input())
k = int(input())

left = 1
right = k
ans = 0

while left <= right:
    middle_index = (left + right) // 2
    count = 0

    for i in range(1, n + 1):
        count += min(middle_index//i, n)

    if count < k:
        left = middle_index + 1
    else:
        ans = middle_index
        right = middle_index - 1

print(ans)
