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
    q.append((0, 0))
    visit = {}
    visit[(0, 0)] = True
    length = 0

    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return length
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if (nx, ny) not in visit and matrix[nx][ny] == 0:
                q.append((nx, ny))
                visit[(nx, ny)] = True
        length += 1


result = bfs()

pass