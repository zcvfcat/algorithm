from collections import deque

d = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def solution(arr: list[list[int]]):
    distances = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    h, w = len(arr), len(arr[0])
    end = (h - 1, w - 1)

    def in_boundary(y, x):
        return 0 <= y < h and 0 <= x < w

    q = deque([(0, 0, 0)])

    tmp = 0

    while q:
        y, x, d_i = q.popleft()
        if tmp == 32:
            break
        tmp += 1
        print(y, x)
        if (y, x) == end:
            return distances[y][x]

        for i in range(4):
            dy, dx = d[(d_i + i) % 4]
            ky, kx = d[(d_i + i - 1) % 4]

            ny, nx = y + dy, x + dx
            kky, kkx = y + ky, x + kx

            # case 1, 벽이 존재할 경우
            if in_boundary(ny, nx) and (not in_boundary(kky, kkx) or arr[kky][kkx] == 1):
                distances[ny][nx] = distances[y][x] + 1
                q.append((ny, nx, i))
                break

            # case 2, 벽이 없을 경우
            if in_boundary(kky, kkx) and arr[kky][kkx] == 0 and d_i != (d_i + i - 1):
                distances[ny][nx] = distances[y][x] + 1
                q.append((ny, nx, i))
                break

    return None


arr = [[0, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0]]
result = solution(arr)
print(result)
