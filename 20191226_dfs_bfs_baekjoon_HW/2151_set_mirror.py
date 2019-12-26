#-*- coding:utf-8 -*-

"""
2151 거울 설치

#는 문 두곳
.은 아무 것도 없고 빛이 통과
!는 거울을 설치할 수 있는 위치
*는 벽

거울을 설치하면 45도 꺾인다.

설치해야할 거울의 최소 개수를 출력

알고리즘: BFS

1. 문 두개 위치 구하기
2. !가 나올 때까지 계속 앞으로 가기
3. ! 나오면 꺾거나 직진
"""
from collections import deque
import sys
read = sys.stdin.readline
n = int(read().strip())
home = [list(read().strip()) for _ in range(n)]
q = deque()

check = [[[-1]*4 for _ in range(n)] for _ in range(n)]
door = []
for i, row in enumerate(home):
    for j, v in enumerate(row):
        if v == '#':
            if not q:
                for k in range(4):
                    q.append((i, j, k))
                    check[i][j][k] = 0
            else:
                ex, ey = i, j
            home[i][j] = '!'


def move(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y, z = q.popleft()
        if x == ex and y == ey:
            print(check[x][y][z])
            return
        dx, dy = dxy[z][0], dxy[z][1]
        nx, ny = x + dx, y + dy
        while move(nx, ny) and home[nx][ny] == '.':
            nx, ny = nx + dx, ny + dy
        if move(nx, ny) and home[nx][ny] == '!':
            q.append((nx, ny, z))
            check[nx][ny][z] = check[x][y][z]
            direction = 2 if z < 2 else 0
            for a in range(direction, direction+2):
                if check[nx][ny][a] == -1:
                    q.append((nx, ny, a))
                    check[nx][ny][a] = check[nx][ny][z] + 1


bfs()
