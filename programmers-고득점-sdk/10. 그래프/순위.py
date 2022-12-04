from collections import defaultdict


def solution(n, edges):
    ans = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in edges:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)

    for people in range(1, n + 1):

        for winner in win_graph[people]:
            lose_graph[winner].update(lose_graph[people])

        for loser in lose_graph[people]:
            win_graph[loser].update(win_graph[people])

    for people in range(1, n + 1):
        if len(win_graph[people]) + len(lose_graph[people]) == n - 1:
            ans += 1

    return ans


print(solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2)
