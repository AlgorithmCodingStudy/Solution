"""
17143 낚시왕

낚시왕이 맨 왼쪽부터 차례로 한칸씩 이동하며 낚시를 한다.
1. 오른쪽으로 한칸 이동
2. 땅에서 가장 가까운 상어 잡기
3. 상어들 이동
상어가 겹치면 크기가 가장 큰 상어가 나머지를 잡아먹는다.
낚시왕이 끝까지 이동한 후 잡은 상어의 크기의 합을 구하라.

알고리즘: 시뮬레이션

1. 반복
    1. 오른쪽으로 한칸 이동
    2. 가까운 상어 잡기
    3. 상어들 이동
"""

import sys
read = sys.stdin.readline

r, c, m = map(int, read().strip().split())
if m == 0:
    print(0)
    sys.exit(0)
sharks = [list(map(int, read().strip().split())) for _ in range(m)]
sharks.sort()
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_shark(column):
    for x, y, s, d, z in sharks:
        if y == column:
            global sum_shark
            sum_shark += z
            sharks.remove([x, y, s, d, z])
            return


def move_shark():
    def move(nx, ny, nd):
        dx, dy = dxy[nd-1]
        if nd <= 2:
            s_remain = s % (2*r)
        else:
            s_remain = s % (2*c)
        for _ in range(s_remain):
            nx, ny = nx+dx, ny+dy
            if not (1 <= nx <= r and 1 <= ny <= c):
                dx, dy = -dx, -dy
                nx, ny = nx+2*dx, ny+2*dy
                nd = nd-1 if nd % 2 == 0 else nd+1
        return nx, ny, nd

    nxt_sharks = []
    for x, y, s, d, z in sharks:
        x, y, d = move(x, y, d)
        nxt_sharks.append([x, y, s, d, z])
    nxt_sharks.sort()

    bx, by, bz = -1, -1, -1
    last_sharks = []
    for x, y, s, d, z in nxt_sharks:
        if (bx, by) == (x, y):
            if bz > z:
                continue
            else:
                last_sharks.pop()
                last_sharks.append([x, y, s, d, z])
        else:
            last_sharks.append([x, y, s, d, z])

    return last_sharks


sum_shark = 0
for j in range(c):
    get_shark(j+1)
    sharks = move_shark()
print(sum_shark)
