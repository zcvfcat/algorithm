trial = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
height = len(trial)

for y in range(1, height):
    row = trial[y]
    for x in range(len(row)):
        if x == 0:
            trial[y][x] += trial[y - 1][0]
        elif x == len(row) - 1:
            trial[y][x] += trial[y - 1][-1]
        else:
            trial[y][x] += max(trial[y - 1][x - 1], trial[y - 1][x])

print(trial)
