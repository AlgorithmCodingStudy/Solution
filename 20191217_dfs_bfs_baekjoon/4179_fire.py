#-*- coding:utf-8 -*-

"""
4179 불!

미로에서 탈출을 해야하는데 불이 번진다.
불은 사방으로 한칸씩 번진다.
#은 벽, .는 지나갈 수 있는 공간, J는 출발지점, F는 불의 출발지점

불에 따라잡히면 IMPOSSIBLE
탈출하면 가장 짧은 시간

알고리즘: DFS or BFS

최단시간이면 BFS 아닌가?

1. 불이 움직일 수 있는 곳을 파악하고 이동한다.
2. 지훈이가 움직일 수 있는 곳을 파악하고 이동한다.
3. 반복하며 가장자리에 도달한다면 그때 length를 출력한다.
"""
from sys import stdin
from collections import deque
input = stdin.readline

r, c = map(int, input().split())
m = [list(input().strip()) for _ in range(r)]
dist = [[0]*c for _ in range(r)]
q = deque()
for i in range(r):
    for j in range(c):
        if m[i][j] == 'J':
            sx, sy = i, j
        elif m[i][j] == 'F':
            q.append((i, j, 1))
            dist[i][j] = 1


def bfs():
    q.append((sx, sy, 0))
    dist[sx][sy] = 1
    while q:
        x, y, f = q.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                if f:
                    continue
                print(dist[x][y])
                return
            if not dist[nx][ny] and m[nx][ny] != '#':
                q.append((nx, ny, f))
                dist[nx][ny] = dist[x][y]+1
    print("IMPOSSIBLE")


bfs()
