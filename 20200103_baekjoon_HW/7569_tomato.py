"""
7569 토마토

보관 후 하루가 지나면 상하좌우 위아래의 토마토가 익는다.
며칠이 지나면 토마토들이 모두 익는지 출력
상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
M N H

알고리즘: BFS
"""

from collections import deque
import sys
read = sys.stdin.readline

m, n, h = map(int, read().strip().split())
ripe = []
empty = 0
box = [[[] for _ in range(n)] for _ in range(h)]  # box[z][y][x]
for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, read().strip().split()))
        for k in range(m):
            if box[i][j][k] == 1:
                ripe.append((i, j, k))
            elif box[i][j][k] == -1:
                empty += 1
non_ripe = m*n*h - empty - len(ripe)
if non_ripe == 0:
    print(0)
    sys.exit(0)

visit = [[[-1]*m for _ in range(n)] for _ in range(h)]
dzyx = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def bfs():
    q = deque()
    for z, y, x in ripe:
        q.append((z, y, x))
        visit[z][y][x] = 1

    ripe_cnt = 0
    while q:
        z, y, x = q.popleft()

        for dz, dy, dx in dzyx:
            nz, ny, nx = z+dz, y+dy, x+dx
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if visit[nz][ny][nx] == -1 and box[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = visit[z][y][x] + 1
                    q.append((nz, ny, nx))
                    ripe_cnt += 1
                    if ripe_cnt == non_ripe:
                        return visit[z][y][x]
    return -1


print(bfs())
