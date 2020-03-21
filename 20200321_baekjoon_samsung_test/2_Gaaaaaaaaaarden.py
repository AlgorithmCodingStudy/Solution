"""
2 Gaaaaaaaaaarden

정원에 초록색 배양액과 빨간색 배양액을 뿌린다.
파란색 땅은 호수
노란색 땅은 배양액을 뿌릴 수 있는 땅
하얀색 땅은 그냥 땅

노란색 땅에 배양액을 뿌리면 배양액이 번져나간다.
만약 초록색 배양액과 빨간색 배양액이 동시에 만나면 꽃이 핀다.
꽃이 핀 개수를 출력하라.
"""
from copy import deepcopy
from itertools import combinations
import sys
read = sys.stdin.readline

n, m, g, r = map(int, read().split())
area = []
choice = []
for a in range(n):
    area.append(list(map(int, read().split())))
    for b in range(m):
        if area[a][b] == 2:
            choice.append((a, b))


def spread():
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = []
    for x, y in green:
        q.append((x, y, 3))
    for x, y in red:
        q.append((x, y, 4))

    cnt = 0

    while q:
        new_q = {}
        for x, y, color in q:
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not(0 <= nx < n and 0 <= ny < m):
                    continue
                if now_area[nx][ny] == 1 or now_area[nx][ny] == 2:
                    if (nx, ny) in new_q:
                        new_q[(nx, ny)].add(color)
                    else:
                        new_q[(nx, ny)] = set([color])

        new_q2 = []
        for x, y in new_q:
            if len(new_q[(x, y)]) >= 2:
                now_area[x][y] = 7
                cnt += 1
            else:
                now_area[x][y] = new_q[(x, y)].pop()
                new_q2.append((x, y, now_area[x][y]))

        q = new_q2

    return cnt


cases = list(combinations(choice, g+r))
max_result = 0
for case in cases:
    cases2 = list(combinations(case, g))
    for case2 in cases2:
        green = case2
        red = tuple(set(case) - set(case2))
        now_area = deepcopy(area)

        for a, b in green:
            now_area[a][b] = 3
        for a, b in red:
            now_area[a][b] = 4

        result = spread()
        max_result = max(result, max_result)
print(max_result)
