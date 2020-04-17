"""
2186 문자판

문자판이 주어지고 k가 주어진다.
현재위치에서 상하좌우 k만큼 움직일 수 있다.
주어진 문자열을 만들 수 있는 경로의 개수를 출력하라.

알고리즘: 시뮬레이션

1. 문자열 전체에서 시작 문자를 찾아 출발지점으로 정한다.
2. 현재위치에서 상하좌우 k만큼에서 다음 문자를 찾는다. 있는 만큼 다시 재귀
3. 문자열의 끝까지 도착하면 cnt += 1
"""

import sys
read = sys.stdin.readline

n, m, k = map(int, read().split())
characters = [list(read().strip()) for _ in range(n)]
target = list(read().strip())
target_pos = [[] for _ in range(len(target))]
dxy = []
for k_ in range(1, k+1):
    dxy.extend([(k_, 0), (-k_, 0), (0, k_), (0, -k_)])

for i in range(n):
    for j in range(m):
        for idx in range(len(target)):
            if characters[i][j] == target[idx]:
                target_pos[idx].append((i, j))

graph = {}
for i in range(len(target)-1):
    us, vs = target_pos[i], target_pos[i+1]
    for u, (xu, yu) in enumerate(us):
        for v, (xv, yv) in enumerate(vs):
            dx, dy = xv-xu, yv-yu
            if (dx, dy) in dxy:
                if (xu, yu) not in graph:
                    graph[(xu, yu)] = [(xv, yv)]
                else:
                    graph[(xu, yu)].append((xv, yv))
for u, v in target_pos[-1]:
    graph[(u, v)] = True


def find(x, y, depth):
    if depth == len(target):
        global cnt
        cnt += 1
        return

    for u_, v_ in graph[(x, y)]:
        if (u_, v_) not in graph:
            continue
        find(u_, v_, depth+1)


cnt = 0
for u, v in target_pos[0]:
    find(u, v, 1)
print(cnt)
