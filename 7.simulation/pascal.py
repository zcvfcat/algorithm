def pascal(l):
    tri = [[1 for _ in range(i + 1)] for i in range(l)]
    for i in range(2, l):
        for j in range(1, i):
            tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
    return tri