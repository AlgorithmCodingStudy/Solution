"""
5569 출근 경로

(1, 1)에서 (w, h)로 가는데 북쪽과 동쪽으로만 이동가능하다.
한번 꺾고나면 1블럭 초과 꼭 가야한다.
갈 수 있는 출근 경로를 100000으로 나눈 나머지를 출력하라.

알고리즘: 시뮬레이션, 브루트 포스, DFS

1. 동쪽, 북쪽으로 이동
2. 꺽으면 인자로 turn=false
3. turn이 false면 무조건 직진
4. turn이 true면 두가지 가능
"""

import sys
read = sys.stdin.readline

w, h = map(int, read().strip().split())
cnt = 0
dxy = [(1, 0), (0, 1)]


def dfs(x, y, direction, go):
    if (x, y) == (w, h):
        global cnt
        cnt += 1
        return
    else:
        for now_direction in range(2):
            if go == 0 and direction != now_direction:
                continue
            dx, dy = dxy[now_direction]
            nx, ny = x+dx, y+dy
            if 1 <= nx <= w and 1 <= ny <= h:
                if direction != now_direction:
                    dfs(nx, ny, now_direction, 0)
                else:
                    dfs(nx, ny, now_direction, 1)


dfs(2, 1, 0, 1)
dfs(1, 2, 0, 1)
print(cnt)
