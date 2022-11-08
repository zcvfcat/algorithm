# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 1 2 3 4 5
#       4 5 6
#             7 8
#                                  15

n = int(input())

start = 1
end = 1

count = 1
acc = start
while end != n:
    if acc == n:
        count += 1
        end += 1
        acc += end
    elif acc > n:
        acc -= start
        start += 1
    else:
        end += 1
        acc += end

print(count)
