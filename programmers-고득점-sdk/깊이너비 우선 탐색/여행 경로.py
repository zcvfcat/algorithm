from collections import deque


def solution(tickets):

    tickets.sort(key=lambda x: (x[0], x[1]))
    path = ['ICN']
    visited = [False for _ in range(len(tickets))]

    q = deque([(path, visited)])

    ans = []

    while q:
        path, visited = q.popleft()
        node = path[-1]

        if all(True == element for element in visited):
            ans.append(path)

        for edge_index in range(len(tickets)):
            start_node, end_edge = tickets[edge_index]

            if visited[edge_index]:
                continue

            if start_node == node:
                next_visited = [*visited]
                next_visited[edge_index] = True
                next_path = path + [end_edge]

                q.append((next_path, next_visited))

    return ans[0]


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
