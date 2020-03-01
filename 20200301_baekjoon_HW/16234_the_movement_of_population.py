"""
16234 인구 이동

국경선을 공유하는 두 나라의 차이가 L이상 R이하면 국경 개방
연합인 각 칸의 인구수 = 연합의 인구수 // 연합인 국가 수
인구 이동이 일어나는 횟수를 출력

알고리즘: BFS, 시뮬레이션

1. 인구 이동이 있으면 반복
    1. bfs all로 연합 찾기
    2. 인구 이동이 발생하면 flag true
    3. 안하면 break
"""
from collections import deque
import sys
read = sys.stdin.readline

n, l, r = map(int, read().strip().split())
a = [list(map(int, read().strip().split())) for _ in range(n)]


def bfs_all():
    visit = {}
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def bfs(sx, sy):
        union = [(sx, sy)]
        q = deque([(sx, sy)])
        visit[(sx, sy)] = True
        while q:
            x, y = q.popleft()
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not(0 <= nx < n and 0 <= ny < n):
                    continue
                if (l <= abs(a[x][y] - a[nx][ny]) <= r) and (nx, ny) not in visit:
                    q.append((nx, ny))
                    visit[(nx, ny)] = True
                    union.append((nx, ny))
        return union

    result = []
    for i in range(n):
        for j in range(n):
            if (i, j) in visit:
                continue
            else:
                result.append(bfs(i, j))

    return result


def move():
    movement = False
    for union in unions:
        sum_union = 0
        for x, y in union:
            sum_union += a[x][y]
        sum_union //= len(union)
        for x, y in union:
            if a[x][y] != sum_union:
                a[x][y] = sum_union
                movement = True
    return movement


cnt = 0
while True:
    unions = bfs_all()
    flag = move()
    if not flag:
        break
    cnt += 1

print(cnt)
