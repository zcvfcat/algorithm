# 4-search: 탐색 알고리즘 모음

쉽게 이해할 수 있도록 각 알고리즘의 핵심 아이디어와 사용 예시를 담았습니다.

## 포함 알고리즘

- 선형 탐색 (`linear.py`)
  - `linear_search(arr, target)`: 앞에서부터 순차적으로 비교해 찾음
  - `linear_search_all(arr, target)`: 모든 등장 인덱스 반환
- 이진 탐색 (`binary.py`)
  - `binary_search(arr, target)`: 정렬된 배열에서 대상 인덱스 탐색
  - `lower_bound(arr, target)`: target 이상(>=) 처음 위치
  - `upper_bound(arr, target)`: target 초과(>) 처음 위치
- 삼분 탐색 (`ternary.py`)
  - `ternary_search_real(f, left, right, iterations)`: 연속 구간에서 단봉 함수 최대값 근사
  - `ternary_search_int(f, left, right)`: 정수 구간에서 단봉 함수 최대값 위치
- 문자열 검색
  - `kmp.py`: KMP, 접두사/접미사 테이블로 점프하며 O(n+m)
  - `rabin_karp.py`: 롤링 해시 기반, 평균 O(n+m) (충돌 시 비교)

## 간단 예시

```python
from binary import binary_search, lower_bound, upper_bound

arr = [1, 3, 3, 5, 7]
print(binary_search(arr, 5))   # 3
print(lower_bound(arr, 3))     # 1
print(upper_bound(arr, 3))     # 3
```

```python
from kmp import kmp_search
text, pattern = "ababcabcabababd", "ababd"
print(kmp_search(text, pattern))  # [10]
```

