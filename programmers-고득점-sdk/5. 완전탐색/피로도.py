def solution(k, dungeons):
    edges_length = len(dungeons)
    visited = [False] * (edges_length + 1)

    # def dfs(node, limit, count):
    #     for index in range(edges_length):
    #         edge, weight = dungeons[index]
    #         if limit > weight and not visited[index]:
    #             visited[node] = True
    #             dfs(edge, )
    #             visited[node] = False


print(solution(80, [[80, 20], [50, 40], [30, 10]]) == 3)
