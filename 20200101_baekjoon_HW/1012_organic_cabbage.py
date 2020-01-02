#-*- coding:utf-8 -*-

"""
1012 유기농 배추

구역이 몇개인지 구하는 문제

저번에 DFS로 풀었으니 이번엔 BFS로 풀어보자.

알고리즘: DFS or BFS
"""

from collections import deque
import sys
read = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        qsize = len(q)
        for _ in range(qsize):
            x, y = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if bat[nx][ny] == 1:
                        q.append((nx, ny))
                        bat[nx][ny] = 0

    return 1


t = int(read().strip())
for _ in range(t):
    m, n, k = map(int, read().strip().split())
    bat = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, read().strip().split())
        bat[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if bat[i][j] == 1:
                cnt += bfs((i, j))

    print(cnt)
