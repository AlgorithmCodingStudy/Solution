"""
17144 미세먼지 안녕

미세먼지가 확산하고 공기청정기가 불어 미세먼지가 사라진다.

미세먼지 확산
    상하좌우로 확산
    본인 // 5로 확산
    본인 = 본인 - 본인 // 5 * 확산수

공기청정기 가동
    위는 반시계로 한칸씩 밀기
    아래는 시계로 한칸씩 밀기
    공기청정기로 들어온 미세먼지는 사라짐
    
알고리즘: 시뮬레이션

1. t초 반복
    1. 확산결과 배열 초기화
    2. 미세먼지 search
        1. 미세먼지 상하좌우로 확산해서 확산결과에 add
        2. 미세먼지 본인 값 계산후 확산결과에 add

    3. 위 회전
    4. 아래 회전
"""
from copy import deepcopy
import sys
read = sys.stdin.readline

r, c, t = map(int, read().strip().split())
area = []
air = []
for a in range(r):
    line_ = list(map(int, read().strip().split()))
    area.append(line_)
    for b in range(c):
        if line_[b] == -1:
            air.append((a, b))


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def diffusion():
    for i, line in enumerate(area):
        for j, v in enumerate(line):
            if v == 0: continue
            elif v == -1:
                nxt_area[i][j] = -1
                continue
            nxt = []
            for dx, dy in dxy:
                nx, ny = i+dx, j+dy
                if 0 <= nx < r and 0 <= ny < c and area[nx][ny] != -1:
                    nxt.append((nx, ny))

            dif = v // 5
            for nx, ny in nxt:
                nxt_area[nx][ny] += dif
            nxt_area[i][j] += area[i][j] - dif * len(nxt)


def fresh():
    sx, sy = air[0]
    # 좌
    for i in range(sx-1, 0, -1):
        nxt_area[i][0] = nxt_area[i-1][0]

    # 상
    for j in range(0, c-1):
        nxt_area[0][j] = nxt_area[0][j+1]

    # 우
    for i in range(0, sx):
        nxt_area[i][c-1] = nxt_area[i+1][c-1]

    # 하
    for j in range(c-1, 1, -1):
        nxt_area[sx][j] = nxt_area[sx][j-1]
    nxt_area[sx][sy+1] = 0

    sx, sy = air[1]
    # 좌
    for i in range(sx+1, r-1):
        nxt_area[i][0] = nxt_area[i+1][0]

    # 하
    for j in range(0, c-1):
        nxt_area[r-1][j] = nxt_area[r-1][j+1]

    # 우
    for i in range(r-1, sx, -1):
        nxt_area[i][c-1] = nxt_area[i-1][c-1]

    # 상
    for j in range(c-1, 1, -1):
        nxt_area[sx][j] = nxt_area[sx][j-1]
    nxt_area[sx][sy+1] = 0


for time in range(t):
    nxt_area = [[0]*c for _ in range(r)]

    diffusion()

    fresh()

    area = nxt_area

area[air[0][0]][air[0][1]] = 0
area[air[1][0]][air[1][1]] = 0
result = [sum(line) for line in area]
print(sum(result))