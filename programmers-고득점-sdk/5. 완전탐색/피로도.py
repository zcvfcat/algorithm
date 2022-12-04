ans = 0


def solution(k, dungeons):
    edges_length = len(dungeons)
    visited = [False] * (edges_length)

    def dfs(limit, count):
        global ans
        if ans < count:
            ans = count

        for edge in range(edges_length):
            require, consume = dungeons[edge]

            if limit >= require and not visited[edge]:
                visited[edge] = True
                dfs(limit - consume, count + 1)
                visited[edge] = False

    dfs(k, 0)
    return ans


print(solution(80, [[80, 20], [50, 40], [30, 10]]) == 3)
