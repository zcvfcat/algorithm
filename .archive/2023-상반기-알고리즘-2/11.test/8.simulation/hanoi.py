def hanoi(n, start, end, via):
    if n == 1:
        return [(start, end)]
    else:
        path = hanoi(n - 1, start, via, end)
        path.append((start, end))
        path += hanoi(n - 1, via, end, start)
        return path


path = hanoi(3, 1, 3, 2)
print(path)
