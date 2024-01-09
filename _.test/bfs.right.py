from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def solution(arr):
    h, w = len(arr), len(arr[0])
    end = (h - 1, w - 1)

    def in_boundary(y, x): return 0 <= y < h and 0 <= x < w

    q = deque([(0, 0, 0, 1)])

    while q:
        y, x, d_i, cost = q.popleft()

        if (y, x) == end:
            return cost

        for i in range(4):
            curr_i, prev_i = (d_i + i) % 4, (d_i + i - 1) % 4

            # 가는 방향
            dy, dx = d[curr_i]

            # 짚는 방향
            ky, kx = d[prev_i]

            ny, nx = y + dy, x + dx
            kky, kkx = y + ky, x + kx

            # case 1, 벽이 존재할 경우
            if in_boundary(ny, nx) and (not in_boundary(kky, kkx) or arr[kky][kkx] == 1):
                q.append((ny, nx, curr_i, cost + 1))
                break

            # case 2, 벽이 없을 경우
            if in_boundary(kky, kkx) and arr[kky][kkx] == 0:
                q.append((kky, kkx, prev_i, cost + 1))
                break

    return None


arr = [[0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
result = solution(arr)
print(result)
