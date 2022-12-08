k = int(input())
array = []

for _ in range(k):
    age, name = input().split()
    array.append((int(age), name))

array.sort(key=lambda x: x[0])

for age, name in array:
    print(f'{age} {name}')
