numbers_length, quiz = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

sums = [0]

prev_sum = 0

for i in numbers:
    prev_sum += i
    sums.append(prev_sum)

for i in range(quiz):
    start, end = map(int, input().split(' '))
    print(sums[end] - sums[start - 1])
