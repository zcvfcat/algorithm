def floyd_warshall(n, edges):
    """
    플로이드-워셜: 모든 정점 쌍 최단거리. 음수 간선 가능(음수 사이클은 결과 대각 < 0).

    - 입력:
      n: 정점 수 (0..n-1)
      edges: (u, v, w) 리스트
    - 반환: dist 행렬 (dist[i][j] = i에서 j 최단거리)
    """
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0
    for u, v, w in edges:
        if w < dist[u][v]:
            dist[u][v] = w

    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            row_k = dist[k]
            row_i = dist[i]
            for j in range(n):
                alt = dik + row_k[j]
                if alt < row_i[j]:
                    row_i[j] = alt

    return dist


