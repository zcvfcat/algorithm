# n, m = map(int, input().split(' '))

# numbers = list(map(int, input().split(' ')))
# prefix_numbers = [0] * (n + 1)

# for i in range(n):
#     prefix_numbers[i + 1] = prefix_numbers[i] + numbers[i]

# count = [0] * n

# for i in range(n):
#     for j in range(i + 1, n + 1):
#         k = (prefix_numbers[j] - prefix_numbers[i]) % m

#         if k == 0:
#             count[i] += 1

# print(sum(count))

# 아 시간 초과
# 답 보장~~~

# m = 3
# 1 2 3 1 2 -> input
# 1 3 6 7 9 -> prefix_map 이자 3 나누면 3개 나옴
#   2 5 6 8 -> 1
#     3 4 6 -> 2
#       1 3 -> 1
#         2 -> 0
