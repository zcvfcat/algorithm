# A-B C-D 선분이 ccw 곱이 음수 면 교차
# ccw 가 0일 경우 하나의 선분 max 값과 다른 선분의 min 값을 비교
# 와 모르겠다;;

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def create_ccw(x1, y1, x2, y2, x3, y3):
    ccw = (x1 * y1 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

    if ccw > 0:
        return 1
    elif ccw < 0:
        return -1
    else:
        return 0


def is_overlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and \
            min(x3, x4) <= max(x1, x2) and \
            min(y1, y2) <= max(y3, y4) and \
            min(y3, y4) <= max(y1, y2):
        return True
    return False


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = create_ccw(x1, y1, x2, y2, x3, y3)
    abd = create_ccw(x1, y1, x2, y2, x4, y4)
    cda = create_ccw(x3, y3, x4, y4, x1, y1)
    cdb = create_ccw(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        return is_overlab(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False


cross = is_cross(x1, y1, x2, y2, x3, y3, x4, y4)

if cross:
    print(1)
else:
    print(0)
