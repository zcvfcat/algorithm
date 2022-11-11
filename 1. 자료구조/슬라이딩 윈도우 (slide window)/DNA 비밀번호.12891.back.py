# 안되누...
s, p = map(int, input().split(' '))
dna = input()
hashed_code = dict(
    zip(['A', 'C', 'G', 'T'], list(map(int, input().split(' ')))))

current_code = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
ans = 0


def vertify(current_code):
    if hashed_code['A'] >= current_code['A'] and hashed_code['C'] >= current_code['C'] and hashed_code['G'] >= current_code['G'] and hashed_code['T'] >= current_code['T']:
        return True
    else:
        return False


for i in range(p - 1):
    current_code[dna[i]] += 1

for i in range(p - 1, s):
    current_code[dna[i]] += 1

    if vertify(current_code):
        ans += 1
    current_code[dna[i - p + 1]] -= 1

print(ans)
