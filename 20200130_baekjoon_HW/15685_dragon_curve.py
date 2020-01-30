"""
15685 드래곤 커브

NxN에 드래곤 커브를 그리는데 그리고나서 1x1 사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 사각형의 개수를 구해라.
즉 드래곤 커브를 그리고나서 (0, 0), (0, 1), (1, 0), (1, 1)이 모두 사용됐으면 이 사각형은 체크

알고리즘: 재귀

1. 드래곤커브를 각각 그리자.
    1. 그려가는 path를 저장하자.
        0 세대 [(0, 0), (1, 0)]
        1 세대 [(0, 0), (1, 0), (1, -1)]
        2 세대 [(0, 0), (1, 0), (1, -1), (0, -1), (0, -2)]
        90도를 꺾으면 현재와 다음 차이가 x, y 바꾸고 부호도 바꾼다.
2. 합치자.
3. 모두 사용된 곳을 조사하자.

3 3 0 1
0 [33, 43]
1 [33, 43, 42]

4 2 1 3
0 [42, 41,
2 [33, 43, 42, 32, 31]

회전변환
x' = (x-a)*cosR - (y-b)*sinR
y' = (x-a)*sinR + (y-b)*cosR
x' = (y-b)
y' = -(x-a)
"""

import sys
read = sys.stdin.readline


def dragon_curve(k_now, curves):
    if k_now == g:
        return curves
    else:
        center = curves[-1]
        for point in reversed(curves[:-1]):
            dx, dy = -(point[1] - center[1]), (point[0] - center[0])
            nx, ny = center[0]+dx, center[1]+dy
            curves.append((nx, ny))
        curves = dragon_curve(k_now+1, curves)
        return curves


dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
curve_all = []
n = int(read().strip())
for _ in range(n):
    x, y, d, g = map(int, read().strip().split())
    x2, y2 = x+dxy[d][0], y+dxy[d][1]
    curve = dragon_curve(0, [(x, y), (x2, y2)])
    curve_all.extend(curve)

curve_all = sorted(list(set(curve_all)))
cnt = 0
for x, y in curve_all:
    if (x+1, y) not in curve_all:
        continue
    if (x, y+1) not in curve_all:
        continue
    if (x+1, y+1) not in curve_all:
        continue
    cnt += 1
print(cnt)
