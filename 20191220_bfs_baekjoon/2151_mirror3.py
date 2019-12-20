#-*- coding:utf-8 -*-

"""
2151 거울 설치

거울을 설치할 건데 한 쪽 문에서 다른 쪽 문을 볼 수 있도록
5
***#*
*.!.*
*!.!*
*.!.*
*#***

#는 문이고 항상 두개
.은 아무것도 없는 곳으로 빛이 통과
!는 거울을 설치할 수 있는 지점
*는 벽

설치해야 할 거울의 최소 개수 출력

알고리즘: BFS

1. 문 두 개 위치 구해 먼저 나온 것을 q에 append
2. dist[x][y][이동방향] -1로 초기화
2. BFS
    1.x, y, z를 popleft
    2. 만약 현재 노드가 다른 문이라면 종료
    3. 현재 이동방향으로 다음 노드가 .이라면 계속 이동
    4. !가 나오면 새로운 노드에 현재 노드의 거울 수를 복사
    5. 새로운 노드를 q에 append
    6. 새로운 노드 기준으로 90도 회전한 곳을 방문하지 않았다면 거울 수의 1을 더하여 입력하고 q에 append
    7. 반복
"""

import sys
read = sys.stdin.readline
from collections import deque


def move(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


def bfs():
    while q:
        x, y, z = q.popleft()
        if x == ex and y == ey:
            print(dist[x][y][z])
            return
        nx, ny = x+dx[z], y+dy[z]
        while move(nx, ny) and room[nx][ny] == '.':
            nx, ny = nx+dx[z], ny+dy[z]
        if move(nx, ny) and room[nx][ny] == '!':
            dist[nx][ny][z] = dist[x][y][z]
            q.append((nx, ny, z))
            k = 2 if z < 2 else 0
            for i in range(k, k+2):
                if dist[nx][ny][i] == -1:
                    dist[nx][ny][i] = dist[x][y][z]+1
                    q.append((nx, ny, i))


dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
n = int(read().strip())
room = [list(read().strip()) for _ in range(n)]
dist = [[[-1]*4 for _ in range(n)] for _ in range(n)]
q = deque()

for i, row in enumerate(room):
    for j, v in enumerate(row):
        if v == '#':
            if not q:
                for k in range(4):
                    q.append((i, j, k))
                    dist[i][j][k] = 0
            else:
                ex, ey = i, j
            room[i][j] = '!'

bfs()
