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
area = [[[] for _ in range(c)] for _ in range(r)]
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i, j, s_, d_, z_ in sharks:
    area[i-1][j-1].append(z_)


def get_shark(column):
    for x, y, s, d, z in sharks:
        if y == column:
            global sum_shark
            sum_shark += z
            sharks.remove([x, y, s, d, z])
            return


def move_shark():
    for idx, [x, y, s, d, z] in enumerate(sharks):
        x, y = x-1, y-1
        dx, dy = dxy[d-1]
        if z in area[x][y]:
            nx, ny = x + s*dx, y + s*dy

            if d == 1 or d == 2:
                if not 0 <= nx < r:
                    if nx < 0:
                        nx = abs(nx)

                    if (nx // (r-1)) % 2 == 0:
                        d = 2
                        nx = nx % (r-1)
                    else:
                        d = 1
                        nx = (r-1) - nx % (r-1)

            else:
                if not 0 <= ny < c:
                    if ny < 0:
                        ny = abs(ny)

                    if (ny // (c-1)) % 2 == 0:
                        d = 3
                        ny = ny % (c-1)
                    else:
                        d = 4
                        ny = (c-1) - ny % (c-1)
            area[x][y].remove(z)
            area[nx][ny].append(z)
            sharks[idx] = nx+1, ny+1, s, d, z


sum_shark = 0
for j in range(c):
    for i in range(r):
        if area[i][j]:
            sum_shark += area[i][j].pop()
            break
    move_shark()
    for i in range(r):
        for k in range(c):
            if area[i][k]:
                area[i][k] = [max(area[i][k])]
print(sum_shark)
