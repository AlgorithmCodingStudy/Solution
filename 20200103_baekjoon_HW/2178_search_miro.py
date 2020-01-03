#-*- coding:utf-8 -*-

"""
2178 미로탐색

미로에서
1은 이동할 수 있는 칸
0은 이동할 수 없는 칸
(1, 1) -> (N, M)까지 지나야 하는 칸의 수 출력

알고리즘: BFS
"""
from collections import deque
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
miro = [list(map(int, read().strip())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs():
    q = deque()
    q.append((0, 0))
    cnt = 2

    while q:
        qsize = len(q)
        for _ in range(qsize):
            x, y = q.popleft()
            miro[x][y] = 0
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if miro[nx][ny] == 1:
                        if (nx, ny) == (n - 1, m - 1):
                            return cnt
                        q.append((nx, ny))
        cnt += 1


visit = [[0]*m for _ in range(n)]


def bfs2():
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (n-1, m-1):
            return visit[x][y]

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == 0 and miro[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))


print(bfs2())
