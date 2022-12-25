from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for start, end in sorted(tickets):
            graph[start].append(end)

        route, stack = [], ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))

            route.append(stack.pop())

        return route[::-1]
