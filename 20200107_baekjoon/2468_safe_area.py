"""
2468 안전 영역

비가 어느 정도 내려서 땅이 물에 잠기는데 잠기지 않는 구역을 안전 영역이라고 한다.
비의 양에 따라 안전 영역의 개수가 최대가 되는 개수를 구해보자.

알고리즘: BFS or DFS

1. 지역의 min에서 max-1까지 완전 탐색을 한다.
    1. BFS all
    2. 영역의 개수를 비교하여 최댓값을 저장한다.
"""

from collections import deque
import sys
read = sys.stdin.readline

n = int(read().strip())
area = [list(map(int, read().strip().split())) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start):
    q = deque()
    q.append(start)
    visit[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visit[nx][ny] == 0 and area[nx][ny] > rain:
                q.append((nx, ny))


def dfs(start):
    q = deque()
    q.append(start)
    visit[start[0]][start[1]] = 1

    while q:
        x, y = q.pop()
        visit[x][y] = 1
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visit[nx][ny] == 0 and area[nx][ny] > rain:
                q.append((nx, ny))


min_area, max_area = min(min(area)), max(max(area))
max_cnt = 1
for rain in range(min_area, max_area):
    cnt = 0
    visit = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and area[i][j] > rain:
                dfs((i, j))
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt


print(max_cnt)
