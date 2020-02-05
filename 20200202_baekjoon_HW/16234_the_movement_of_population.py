"""
16234 인구 이동

국가 사이의 인구가 L이상 R이하라면 국경이 열린다.
국경이 열려 이동할 수 있는 국가들은
인구수 합 // 국가 수 로 인구가 바뀐다.
인구이동이 몇번 발생하는지 구하라.

알고리즘: 시뮬레이션, DFS

1. 더이상 인구이동이 없을때까지 반복
    1. 방문하지 않은 곳
        1. DFS를 시작해서 연합이 될 수 있는 곳을 모두 탐색 & 방문 체크
        2. 연합인 곳의 인구수를 업데이트

처음에 연합이 4개면 move 0
처음에 연합이 1개면 move 1
두번째에 연합이 4개면 현재 move
두번째에 연합이 1개면 현재 move+1

"""

import sys
input = sys.stdin.readline

n, l, r = map(int, input().strip().split())
nations = [list(map(int, input().strip().split())) for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(sx, sy):
    stack = [(sx, sy)]
    union = [(sx, sy)]
    union_sum = nations[sx][sy]

    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in union and l <= abs(nations[x][y]-nations[nx][ny]) <= r:
                    union.append((nx, ny))
                    stack.append((nx, ny))
                    union_sum += nations[nx][ny]
    return union, union_sum


def union_update():
    population = now_sum // len(now_union)
    for x, y in now_union:
        nxt[x][y] = population


move = 0
before_unions = []
while True:
    nxt = [[0]*n for _ in range(n)]
    visit = []
    unions = []
    unions_sum = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in visit:
                now_union, now_sum = dfs(i, j)
                unions.append(now_union)
                visit.extend(now_union)
                union_update()

    if len(unions) == n*n:
        break
    if before_unions == unions:
        break

    before_unions = unions
    nations = nxt
    move += 1

print(move)
