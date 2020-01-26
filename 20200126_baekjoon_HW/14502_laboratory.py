"""
14502 연구소

벽을 3개 세우고 바이러스가 퍼진 후 안전영역의 넓이의 최대를 구하라.

알고리즘: DFS or BFS

1. 벽 3개를 세울 위치의 조합을 모두 구하자.
2. 벽 3개 조합을 하나하나 다 검사하자.
    1. 벽을 세운다.
    2. 바이러스를 퍼트린다.
    3. 0의 개수를 구한다.
    4. 비교한다.
"""
from copy import deepcopy
from itertools import combinations
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
lab = []
zeros, virus = [], []
for i in range(n):
    lab.append(list(map(int, read().strip().split())))
    for j, v in enumerate(lab[i]):
        if v == 0:
            zeros.append((i, j))
        elif v == 2:
            virus.append((i, j))

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def spread_virus(sx, sy):
    def check_range(x_, y_):
        return 0 <= x_ < n and 0 <= y_ < m

    stack = [(sx, sy)]

    while stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not check_range(nx, ny):
                continue
            if now_lab[nx][ny] == 0:
                stack.append((nx, ny))
                now_lab[nx][ny] = 2


def count_zeros():
    cnt = 0
    for row in now_lab:
        cnt += row.count(0)
    return cnt


trial = combinations(zeros, 3)
max_cnt = 0
for w1, w2, w3 in trial:
    now_lab = deepcopy(lab)
    now_lab[w1[0]][w1[1]] = 1
    now_lab[w2[0]][w2[1]] = 1
    now_lab[w3[0]][w3[1]] = 1

    for a, b in virus:
        spread_virus(a, b)

    now_cnt = count_zeros()
    if now_cnt > max_cnt:
        max_cnt = now_cnt

print(max_cnt)
