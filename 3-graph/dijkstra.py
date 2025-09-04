import heapq


def dijkstra(graph, start):
    """
    다익스트라 알고리즘(음수 간선 없음): 한 정점에서 모든 정점까지 최단거리.

    - 입력: graph는 dict[node] = [(neighbor, weight), ...]
    - 반환: (dist, parent)
      dist[node] = start에서 node까지의 최단거리(없으면 float('inf'))
      parent[node] = 최단경로 상에서의 이전 정점
    """
    dist = {node: float('inf') for node in graph}
    parent = {start: None}
    dist[start] = 0.0
    pq = [(0.0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if cur_dist > dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = cur_dist + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, parent


