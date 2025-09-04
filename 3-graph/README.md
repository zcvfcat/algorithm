# 3-graph: 그래프 알고리즘 모음

이 폴더에는 기본적인 그래프 알고리즘 구현과 간단한 설명이 포함되어 있습니다.

## 포함 알고리즘

- BFS/DFS (`bfs_dfs.py`)
  - `bfs(graph, start)` : 너비 우선 탐색, 최단 간선 수 거리 탐색에 유용
  - `dfs_iterative(graph, start)`, `dfs_recursive(graph, start)` : 깊이 우선 탐색
- 다익스트라 (`dijkstra.py`)
  - `dijkstra(graph, start)` : 음수 가중치가 없는 그래프의 단일 출발 최단거리
- 벨만-포드 (`bellman_ford.py`)
  - `bellman_ford(n, edges, source)` : 음수 간선/사이클 처리 가능, 최단거리 및 사이클 탐지
- 플로이드-워셜 (`floyd_warshall.py`)
  - `floyd_warshall(n, edges)` : 모든 정점 쌍 최단거리
- 위상 정렬 (`toposort.py`)
  - `toposort_kahn(n, edges)` : DAG에서의 위상 순서. 사이클 시 예외 발생
- MST (`mst.py`)
  - `kruskal(n, edges)` : 크루스칼 최소 신장 트리
  - `prim(n, adj, start=0)` : 프림 최소 신장 트리
- DSU (`dsu.py`)
  - `DisjointSetUnion` : 경로압축 + 랭크

## 그래프 입력 형식

- 인접 리스트(dict): `{u: [(v, w), ...], ...}` 혹은 `{u: [v1, v2, ...], ...}`
- 간선 리스트: `[(u, v, w), ...]` 또는 가중치가 앞에 오는 `[(w, u, v), ...]`

## 간단 예시

```python
from bfs_dfs import bfs
from dijkstra import dijkstra

graph_unweighted = {0:[1,2], 1:[2], 2:[0,3], 3:[]}
order, parent = bfs(graph_unweighted, 0)

graph_weighted = {0:[(1,2),(2,5)], 1:[(2,1)], 2:[]}
dist, parent = dijkstra(graph_weighted, 0)
```
