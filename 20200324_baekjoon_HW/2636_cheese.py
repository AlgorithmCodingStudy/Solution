"""
2636 치즈

치즈가 바깥부터 녹아가는데 안에 있는 구멍은 공기가 없어서 안녹는다.
다 녹는데 걸리는 시간과 다 녹기전에 치즈 수를 출력하라.

알고리즘: BFS

1. 겉에 공기에 대하여 BFS를 진행한다.
"""
from copy import deepcopy
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
area = [list(map(int, read().split())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
c = 0
for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            c += 1


def find_boundary(now_q):
    boundary = []
    while now_q:
        new_q = []
        for x, y in now_q:
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not(0 <= nx < n and 0 <= ny < m):
                    continue
                if (nx, ny) not in visit and area[nx][ny] == 0:
                    new_q.append((nx, ny))
                    visit[(nx, ny)] = True
                elif (x, y) not in boundary and area[nx][ny] == 1:
                    boundary.append((x, y))
        now_q = new_q

    return boundary


def eat(now_q):
    new_q = []
    for x, y in now_q:
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if (nx, ny) not in visit and area[nx][ny] == 1:
                new_q.append((nx, ny))
                visit[(nx, ny)] = True
                area[nx][ny] = 0
                global c
                c -= 1
    return new_q


visit = {}
q = []
for i in range(n):
    q.append((i, 0))
for j in range(1, m - 1):
    q.append((0, j))

t = 1
while True:
    last_area = deepcopy(area)
    q = find_boundary(q)
    q = eat(q)
    if c == 0:
        break
    t+=1
print(t)
cnt = 0
for i in range(n):
    for j in range(m):
        if last_area[i][j] == 1:
            cnt += 1
print(cnt)
