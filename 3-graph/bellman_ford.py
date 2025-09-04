def bellman_ford(n, edges, source):
    """
    벨만-포드 알고리즘: 음수 간선/음수 사이클 탐지 가능.

    - 입력:
      n: 정점 수 (0..n-1)
      edges: (u, v, w) 리스트
      source: 시작 정점
    - 반환: (dist, parent, has_negative_cycle)
      dist[i]: source에서 i까지 최단거리(없으면 float('inf'))
      parent[i]: 최단경로 상 이전 정점
      has_negative_cycle: 음수 사이클 존재 여부
    """
    dist = [float('inf')] * n
    parent = [None] * n
    dist[source] = 0.0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, parent, has_negative_cycle


