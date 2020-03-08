"""
17837 새로운 게임2

말들이 1부터 k번째말까지 이동을 한다.
말이 이동하려는 칸이
    흰색이면
    쌓여있는 말 전부 이동

    빨간색이면
    쌓여있는 말 전부 이동하는데 뒤집는다.

    파란색이면
    방향바꾸고 한칸 이동한다.
    다 데리고 가나 안데리고 가나?
    한칸 이동하려는 곳이 또 파란색이면 방향만 바꾸고 끝

알고리즘 : 시뮬레이션

1. 턴을 기준으로 반복
    1. 말을 하나씩 이동 (리스트에 위치만 전부 저장)
        1. 다음 이동할 위치가
            1. 흰색이면 쌓여잇는 말 전부 이동 (area에 리스트 형태로 쌓기)
            2. 빨간색이면 뒤집어서 이동
            3. 파란색이면 방향 바꾸고 한칸 이동
"""

import sys
read = sys.stdin.readline

n, k = map(int, read().strip().split())
area = [list(map(int, read().strip().split())) for _ in range(n)]
markers = [list(map(lambda x: int(x)-1, read().strip().split())) for _ in range(k)]
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def set_markers():
    a = [[[] for _ in range(n)] for _ in range(n)]
    for i_, (x_, y_, d_) in enumerate(markers):
        a[x_][y_].append([i_, x_, y_, d_])

    return a


area_markers = set_markers()

for turn in range(1000):
    for i, (x, y, d) in enumerate(markers):
        nx, ny = x+dxy[d][0], y+dxy[d][1]
        idx = area_markers[x][y].index([i, x, y, d])
        length = len(area_markers[x][y]) - idx
        if not(0 <= nx < n and 0 <= ny < n) or area[nx][ny] == 2:
            nd = d+1 if d % 2 == 0 else d-1
            nx, ny = x+dxy[nd][0], y+dxy[nd][1]
            if not(0 <= nx < n and 0 <= ny < n) or area[nx][ny] == 2:
                nx, ny = x, y
                pos = idx
            elif area[nx][ny] == 0:
                pos = idx
            else:
                pos = -1

        elif area[nx][ny] == 0:
            nd = d
            pos = idx

        else:
            nd = d
            pos = -1
        area_markers[x][y][idx][-1] = nd
        for j in range(length):
            if pos != -1:
                now = area_markers[x][y].pop(idx)
            else:
                now = area_markers[x][y].pop()
            area_markers[nx][ny].append([now[0], nx, ny, now[-1]])
            markers[now[0]] = [nx, ny, now[-1]]

        if len(area_markers[nx][ny]) >= 4:
            print(turn+1)
            sys.exit(0)
print(-1)
