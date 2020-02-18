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


def dfs(x, y, direction):
    if (x, y) == (w, h):
        global cnt
        cnt += 1
        return
    else:
        if direction == 0:
            for i in range(w-x+1):
                if i == 0: continue
                if x+i+1 > w: break
                dfs(x+i+1, y, 1)
        else:
            for j in range(h-y+1):
                if j == 0: continue
                if y+j+1 > h: break
                dfs(x, y+j+1, 0)


dfs(2, 1, 0)
dfs(2, 1, 1)
dfs(1, 2, 0)
dfs(1, 2, 1)
print(cnt)
