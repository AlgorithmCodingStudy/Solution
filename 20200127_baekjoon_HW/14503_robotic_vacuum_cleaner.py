"""
14503 로봇 청소기

로봇 청소기가 청소하는 영역을 구하라.
청소기는 동서남북중 한 곳을 바라본다.

1. 현재 위치를 청소한다.
2. 현재 위치를 기준으로 왼쪽 방향으로 탐색
    a. 왼쪽 방향에 청소하지 않은 곳이 있다면 왼쪽으로 한칸 진행후 1번부터 다시 진행.
    b. 왼쪽 방향에 청소할 곳이 없다면 왼쪽으로 돌고 다시 2번
    c. 네 방향 모두 청소할 곳이 없거나 벽이면 바라보는 방향 기준으로 후진하고 다시 2번 진행
    d. 네 방향 모두 청소할 곳이 없거나 벽인데 후진도 못하면 작동 정지

알고리즘: 시뮬레이션
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
x, y, d = map(int, read().strip().split())
area = [list(map(int, read().strip().split())) for _ in range(n)]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_range(x_, y_):
    return 0 <= x_ < n and 0 <= y_ < m


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


while True:
    # 1.
    flag_1 = False
    area[x][y] = 2
    # 2.
    for i in range(4):  # b, c, d
        turn_left()
        # a, b, c, d.
        dx, dy = dxy[d]
        nx, ny = x+dx, y+dy
        if check_range(nx, ny):
            if area[nx][ny] == 0:  # a.
                x, y = nx, ny
                flag_1 = True
                break
    if flag_1:
        continue
    nd = d - 2  # c, d.
    if nd < 0:
        nd += 4
    dx, dy = dxy[nd]
    nx, ny = x+dx, y+dy
    if check_range(nx, ny) and area[nx][ny] == 2:  # c.
        x, y = nx, ny
        continue
    else:  # d.
        break

result = 0
for row in area:
    result += row.count(2)
print(result)
