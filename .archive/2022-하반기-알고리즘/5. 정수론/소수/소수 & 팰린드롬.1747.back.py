N = int(input())
a = [0] * 10000001

for i in range(2, len(a)):
    a[i] = i


for i in range(2, int(len(a) ** 0.5) + 1):

    if a[i] == 0:
        continue

    for j in range(i + i, len(a), i):
        a[j] = 0


def is_palindrome(word: str):
    return word == word[:: -1]


i = N

while True:
    if a[i] != 0:
        target = a[i]

        if is_palindrome(str(target)):
            print(target)
            break
    i += 1
