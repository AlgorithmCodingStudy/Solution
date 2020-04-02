"""
1987 알파벳

0, 0에서 출발하여 상하좌우로 이동하는데 현재 지난 알파벳은 지날 수 없다.
최대 몇칸 이동할 수 있을까

알고리즘: DFS or BFS

"""

import sys
read = sys.stdin.readline

r, c = map(int, read().split())
area = [list(read().strip()) for _ in range(r)]
visit = [0]*26

q = [[0, 0, [area[0][0]]]]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

max_cnt = 0
def dfs(x, y):
    flag = True
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if not(0 <= nx < r and 0 <= ny < c): continue
        idx = ord(area[nx][ny]) - 65
        if not visit[idx]:
            visit[idx] = 1
            dfs(nx, ny)
            visit[idx] = 0
            flag = False
    if flag:
        global max_cnt
        max_cnt = max(max_cnt, sum(visit))

visit[ord(area[0][0]) - 65] = 1
dfs(0, 0)
print(max_cnt)