# 6-dp: 동적 계획법 모음

핵심 아이디어와 간단 예시를 함께 정리했습니다.

## 포함 알고리즘

- 피보나치 (`fibonacci.py`)
  - `fib_memo(n)`: 메모이제이션 (Top-Down)
  - `fib_bottom_up(n)`: 보텀업, O(1) 공간
- 0/1 배낭 (`knapsack_01.py`)
  - `knapsack_01(weights, values, capacity)`: 최대 가치
- 동전 교환 (`coin_change.py`)
  - `min_coins(coins, amount)`: 최소 동전 개수
  - `count_ways(coins, amount)`: 경우의 수(조합)
- LIS (`lis.py`)
  - `lis_length(nums)`: O(n log n) 길이 계산
- LCS (`lcs.py`)
  - `lcs_length(a, b)`: 길이
  - `lcs_string(a, b)`: 문자열 복원
- 편집 거리 (`edit_distance.py`)
  - `edit_distance(a, b)`: Levenshtein 거리
- 최대 부분배열 합 (`kadane.py`)
  - `max_subarray_sum(nums)`: 카데인 알고리즘

## 간단 예시

```python
from fibonacci import fib_bottom_up
print(fib_bottom_up(10))  # 55
```

```python
from knapsack_01 import knapsack_01
print(knapsack_01([2,3,4],[4,5,6],5))  # 9
```

```python
from coin_change import min_coins, count_ways
print(min_coins([1,3,4], 6))   # 2 (3+3 or 2 coins)
print(count_ways([1,2,5], 5))  # 4
```

```python
from lis import lis_length
print(lis_length([10,9,2,5,3,7,101,18]))  # 4
```

```python
from lcs import lcs_length, lcs_string
print(lcs_length("abcde", "ace"))   # 3
print(lcs_string("abcde", "ace"))   # "ace"
```

```python
from edit_distance import edit_distance
print(edit_distance("kitten", "sitting"))  # 3
```

```python
from kadane import max_subarray_sum
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # 6
```

