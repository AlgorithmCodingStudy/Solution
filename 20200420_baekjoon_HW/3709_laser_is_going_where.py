"""
3709 레이저빔은 어디로

레이저를 보드 밖에서 쏘는데
보드 안에는 우향우 거울이 있어서 만나면 오른쪽으로 꺾인다.
최종 도착지는?
만약 빔이 보드 밖을 떠나지 않는다면 출력은 0, 0

알고리즘: 시뮬레이션

1. 현위치와 방향을 가지고 있으면서 계속 전진한다.
2. 우향우 거울을 만나면 방향을 꺾는다.
3. 안만나고 나가면 그 위치를 출력한다.
"""

import sys
read = sys.stdin.readline


def where():
    def range_check(x_, y_):
        return 0 < x_ < n+1 and 0 < y_ < n+1

    def get_start_direction():
        if sx == 0:
            return 2
        elif sx == n+1:
            return 0
        elif sy == 0:
            return 1
        elif sy == n+1:
            return 3

    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    x, y, d = sx, sy, get_start_direction()
    first = True
    while range_check(x, y) or first:
        x, y = x+dxy[d][0], y+dxy[d][1]
        if board[x][y] == 1:
            d += 1
            d = d if d < 4 else 0

        first = False
    return x, y


for _ in range(int(read())):
    n, r = map(int, read().split())
    board = [[0]*(n+2) for _ in range(n+2)]
    for _ in range(r):
        a, b = map(int, read().split())
        board[a][b] = 1
    sx, sy = map(int, read().split())

    print("{} {}".format(*where()))
