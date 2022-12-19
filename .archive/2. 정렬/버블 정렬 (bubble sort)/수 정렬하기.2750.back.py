n = int(input())

l = [0] * n


for i in range(n):
    l[i] = int(input())

# print(sorted(l))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

for i in l:
    print(i)
