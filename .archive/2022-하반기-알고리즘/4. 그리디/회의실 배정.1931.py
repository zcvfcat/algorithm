N = int(input())
A = [[0] * 2 for _ in range(N)]

for i in range(N):
    start, end = map(int, input().split(' '))
    A[i][0] = start
    A[i][1] = end

A.sort(key=lambda x: (x[1], x[0]))

count = 1
end = A[0][1]

for i in range(1, N):
    if A[i][0] >= end:
        count += 1
        end = A[i][1]

print(count)
