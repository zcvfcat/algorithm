from collections import deque


def solution(begin, target, words):
    visited = [False for _ in range(len(words))]
    q = deque([(begin, 0)])
    ans = 0

    while q:
        node, count = q.popleft()

        if node == target:
            ans = count
            break

        for edge_index in range(len(words)):

            if visited[edge_index]:
                continue

            edge = words[edge_index]
            diff = 0

            for char_node, char_edge in zip(node, edge):
                if char_node != char_edge:
                    diff += 1

            if diff == 1:
                visited[edge_index] = True
                q.append((edge, count + 1))

    return ans


print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]) == 4)
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]) == 0)
