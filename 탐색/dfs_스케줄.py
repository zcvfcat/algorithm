from collections import defaultdict

# https://leetcode.com/problems/reconstruct-itinerary/description/
# https://school.programmers.co.kr/learn/courses/30/lessons/43164


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        for start, end in sorted(tickets):
            graph[start].append(end)

        route, stack = [], ['JFK']

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))

            route.append(stack.pop())

        return route[::-1]
