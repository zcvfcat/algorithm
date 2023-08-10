# 두 재료 <- 제한값
# 1 2 3 4 5 7
#   2       7
#     3 4

n = int(input())
m = int(input())
l = list(map(int, input().split(' ')))

l.sort()

start = 0
end = len(l) - 1
count = 0

while start < end:
    if l[start] + l[end] < m:
        start += 1

    elif l[start] + l[end] > m:
        end -= 1

    else:
        start += 1
        end -= 1
        count += 1

print(count)
