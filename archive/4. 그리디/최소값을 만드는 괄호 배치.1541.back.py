a = input().split('-')

total = 0

for i in a[0].split('+'):
    total += int(i)

for i in a[1:]:
    for j in i.split('+'):
        total -= int(j)

print(total)
