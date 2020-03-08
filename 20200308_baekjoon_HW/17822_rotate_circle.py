"""
17822 원판 돌리기

원판을 규칙에 따라 돌리고 합을 출력
원판을 돌리고
    인접하고 같은 수는 모두 0
    인접하고 같은 수가 없으면 판 전체의 평균을 구하고 평균보다 작으면 +1 크면 -1

알고리즘: 시뮬레이션

1. 덱에 숫자 선언
2. x의 배수 원판을 모두 rotate(d)
3. dxy로 인접 확인
4. 인접 처리
"""
from itertools import chain
from collections import deque
import sys
read = sys.stdin.readline

n, m, t = map(int, read().strip().split())
circles = [deque(map(int, read().strip().split())) for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(sx, sy):
    stack = [(sx, sy)]
    visit = {}
    visit[(sx, sy)] = True

    while stack:
        ix, iy = stack.pop()

        for dx, dy in dxy:
            nx, ny = ix+dx, iy+dy
            if not (0 <= nx < n): continue
            elif ny < 0: ny = m-1
            elif ny == m: ny = 0
            if (nx, ny) not in visit and circles[nx][ny] == circles[i][j]:
                stack.append((nx, ny))
                visit[(nx, ny)] = True

    return list(visit.keys())


for _ in range(t):
    x, d, k = map(int, read().strip().split())
    d = -1 if d else 1
    for i in range(x-1, n, x):
        circles[i].rotate(d*k)
    flag = True
    sum_, cnt = 0, 0
    for i in range(n):
        for j in range(m):
            if circles[i][j] == 0: continue
            same = dfs(i, j)

            if len(same) > 1:
                flag = False
                same.append((i, j))
                for nnx, nny in same:
                    circles[nnx][nny] = 0
            else:
                sum_ += circles[i][j]
                cnt += 1
    if flag:
        if cnt == 0: break
        mean = sum_ / cnt
        for i in range(n):
            for j in range(m):
                if 0 < circles[i][j] < mean:
                    circles[i][j] += 1
                elif circles[i][j] > mean:
                    circles[i][j] -= 1

    pass

print(sum(chain(*circles)))
