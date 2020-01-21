"""
14502 연구소

2 바이러스
1 벽
0 빈공간

벽을 3개 세울수 있는데
벽을 3개 세우고 바이러스가 퍼진후 안전영역의 최대값을 출력

알고리즘: DFS or BFS

1. 벽을 어디 3개 세울지 정하자.
    1. 0인 곳을 모두 체크해놓은 후
    2. 조합으로 하나씩 검토
        1. dfs_all
            1. dfs로 2를 모두 퍼트리자.
        2. 0의 갯수를 체크
    3. 최댓값 출력
"""
from itertools import combinations
from copy import deepcopy
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
lab = [list(map(int, read().strip().split())) for _ in range(n)]
zeros = []
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            zeros.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))


dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(start):
    stack = [start]

    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if new_lab[nx][ny] == 0 and (nx, ny) not in walls:
                stack.append((nx, ny))
                new_lab[nx][ny] = 2


def count_zero():
    cnt = 0
    for a in range(n):
        for b in range(m):
            if new_lab[a][b] == 0:
                cnt += 1
    return cnt


cases = list(combinations(zeros, 3))
max_zero = 0
for walls in cases:
    new_lab = deepcopy(lab)
    for v in virus:
        dfs(v)
    count = count_zero() - 3
    if count > max_zero:
        max_zero = count

print(max_zero)
