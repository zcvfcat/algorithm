n, m = map(int, input().split(' '))
videos = list(map(int, input().split(' ')))

left = max(videos)
right = sum(videos)

while left <= right:
    mid_index = (left + right) // 2
    total = 0
    count = 0

    for i in range(n):
        if total + videos[i] > mid_index:
            count += 1
            total = 0

        total += videos[i]

    if total != 0:
        count += 1

    if total > m:
        left = mid_index + 1
    else:
        right = mid_index - 1

print(left)
