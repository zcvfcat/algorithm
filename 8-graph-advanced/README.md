# 9-graph-advanced: 그래프 고급

- `scc.py`: Tarjan SCC 분해
- `bridges_articulation.py`: 브리지/단절점 탐지
- `maxflow_dinic.py`: Dinic 최대 유량
- `bipartite_matching.py`: Hopcroft-Karp 이분 매칭

## 간단 예시

```python
from scc import tarjan_scc
print(tarjan_scc([[1],[2],[0,3],[]]))  # [[2,1,0],[3]] (순서는 다를 수 있음)
```

```python
from bridges_articulation import find_bridges_and_articulation
print(find_bridges_and_articulation(4, [(0,1),(1,2),(2,0),(1,3)]))
```

```python
from maxflow_dinic import Dinic
mf = Dinic(4)
mf.add_edge(0,1,2); mf.add_edge(0,2,1); mf.add_edge(1,3,1); mf.add_edge(2,3,2)
print(mf.max_flow(0,3))
```

```python
from bipartite_matching import hopcroft_karp
print(hopcroft_karp(3,3,[(0,0),(0,1),(1,1),(2,2)]))
```
