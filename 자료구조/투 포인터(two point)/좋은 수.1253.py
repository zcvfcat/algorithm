# 1 2 3 4 5 6 7 8 9 10
#     3 <- 1 + 2
#       4
#         5
#           6
#             7
#               8
#                 9
#                   10

n = int(input())
l = list(map(int, input().split(' ')))

l.sort()

start_idx = 0
end_idx = l.length
