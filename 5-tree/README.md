# 5-tree: 트리 알고리즘 모음

쉽게 이해할 수 있도록 각 알고리즘의 핵심 아이디어와 사용 예시를 담았습니다.

## 포함 알고리즘

- 이진 트리 (`binary_tree.py`)
  - `TreeNode`: 노드 구조체
  - `build_tree_level(values)`: 레벨 순서 배열에서 트리 구성 (None 허용)
  - 순회: `preorder`, `inorder`, `postorder`, `level_order`
  - 유틸: `height`, `size`
- 이진 탐색 트리 (`bst.py`)
  - `BinarySearchTree`: `insert`, `search`, `delete`, `inorder`
- LCA (`lca.py`)
  - `build_rooted_tree(n, edges, root)`: parent, depth, children 구성
  - `lca_parent_depth(u, v, parent, depth)`: 부모/깊이 방식 LCA
- 세그먼트 트리 (`segment_tree.py`)
  - `SegmentTree`: `query(left,right)`, `update(index,value)` — 구간 합 예시
- 펜윅 트리 (`fenwick.py`)
  - `FenwickTree`: `add`, `prefix_sum`, `range_sum`

## 간단 예시

```python
from binary_tree import build_tree_level, inorder
root = build_tree_level([1,2,3,None,4])
print(inorder(root))  # [2, 4, 1, 3]
```

```python
from bst import BinarySearchTree
bst = BinarySearchTree()
bst.insert(5); bst.insert(2); bst.insert(7)
print(bst.inorder())  # [2, 5, 7]
bst.delete(5)
print(bst.inorder())  # [2, 7]
```

```python
from lca import build_rooted_tree, lca_parent_depth
n = 5; edges = [(0,1),(0,2),(1,3),(1,4)]
parent, depth, _ = build_rooted_tree(n, edges, root=0)
print(lca_parent_depth(3, 4, parent, depth))  # 1
```

```python
from segment_tree import SegmentTree
st = SegmentTree([1,2,3,4])
print(st.query(1,3))  # 2+3+4=9
st.update(2, 10)
print(st.query(1,3))  # 2+10+4=16
```

```python
from fenwick import FenwickTree
fw = FenwickTree(5)
fw.add(0, 1); fw.add(3, 2)
print(fw.range_sum(0, 3))  # 3
```

