#-*- coding:utf-8 -*-

"""
2206 벽 부수고 이동하기

(1, 1)에서 (N, M)까지 이동한다.
만약 벽을 부수고 이동할 때 더 짧은 경로가 된다면 벽을 하나까지 부술 수 있다.

최단 거리를 출력하라

알고리즘: BFS

1. 일단 벽을 부수지 않고 최단경로를 구해보자.
"""
from collections import deque
import sys
read = sys.stdin.readline
n, m = map(int, read().strip().split())
matrix = [list(map(int, read().strip())) for _ in range(n)]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visit = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if matrix[nx][ny] == 0 and visit[nx][ny][z] == -1:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append((nx, ny, z))
            if z == 0 and matrix[nx][ny] == 1 and visit[nx][ny][1] == -1:
                visit[nx][ny][z+1] = visit[x][y][z] + 1
                q.append((nx, ny, z+1))

    if visit[n-1][m-1][0] == -1:
        return visit[n-1][m-1][1]
    elif visit[n-1][m-1][1] == -1:
        return visit[n-1][m-1][0]
    else:
        return min(visit[n-1][m-1][0], visit[n-1][m-1][1])


print(bfs())
