"""
7562 나이트의 이동

나이트가 이동하려는 칸이 주어진다.
몇 번의 이동을 통해 이 칸으로 움직일 수 있을까?

알고리즘: BFS

1. 한 변의 길이 l(4 <= l <= 300)
2. 현재 있는 칸
3. 이동하려고 하는 칸
4. BFS
"""

from collections import deque
from sys import stdin
read = stdin.readline

dxy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def bfs():
    q = deque()
    q.append(start)
    visit = [[0]*l for _ in range(l)]

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            print(visit[x][y])
            return

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0 <= nx < l and 0 <= ny < l):
                continue
            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))


t = int(read().strip())
for _ in range(t):
    l = int(read().strip())
    start = tuple(map(int, read().strip().split()))
    end = tuple(map(int, read().strip().split()))
    bfs()
