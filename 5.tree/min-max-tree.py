def build_min_max_tree(lst):
    def build_min_max_t(start, end, l_lst):
        if start == end:
            return [l_lst[start], l_lst[start]]

        if end - start == 1:
            mn = min(l_lst[start], l_lst[end])
            mx = max(l_lst[start], l_lst[end])
            return [mn, mx]

        mid = (start + end) // 2
        l_ret = build_min_max_t(start, mid, l_lst)
        r_ret = build_min_max_t(mid + 1, end, l_lst)

        return [min(l_ret[0], r_ret[0]), max(l_ret[1], r_ret[1])]

    return build_min_max_t(0, len(lst) - 1, lst)

lst = [7, 3, 12, 5, 8, 1, 9]
tree = build_min_max_tree(lst)
print(tree)   # [1, 12]

# Min-Max Tree Algorithm
# ----------------------

# Min-Max Tree는 일반적으로 트리에서 최소값 및 최대 값의 검색 속도를 높여주는 알고리즘이다. 이것은 부분 결정 트리로 줄여지지 않습니다.

# ### 예시

# `7 3 12 5 8 1 9`
# 위와 같은 숫자 리스트가 있을 때, Min-Max Tree는 다음과 같이 만들 수 있다.

# ```
#          1
#       /     \
#     3        9
#   /   \     /   \
# 5     7   8     12
# ```

# ### 구현

# ```python
from math import log2, ceil

# ```

# 위 코드에서 `build_min_max_tree` 함수는 최소, 최대 값을 추적하는 두 개의 값을 반환하는 내부 비공개 함수 `build_min_max_t`를 호출한다. 그리고 재귀를 사용하여 결과 자체를 계산한다. 초기 호출이 완료되면 최소 및 최대 값으로 구성된 리스트가 반환된다.

# 예시:


# ```python

# ```

# 이진 트리의 모양은 위 공식 정해진 모양보다 다르게 나올 수 있다. 그러나 기본적인 아이디어는 동일하다.
