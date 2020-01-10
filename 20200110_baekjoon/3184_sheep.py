"""
3184 양

. 필드
# 울타리
o 양
v 늑대

마당에서 탈출할 수 있는 칸은 어떤 영역에도 속하지 않는다
-> 범위 밖을 이야기하는 건가?

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기게 된다.
-> 이긴다는게 늑대를 몰아내는 건가 아니면 공존하는 건가?

아침이 됐을때 양과 늑대 수 출력

알고리즘: DFS or BFS
"""

import sys
read = sys.stdin.readline

r, c = map(int, read().strip().split())
backyard = [list(read().strip()) for _ in range(r)]
visit = [[False]*c for _ in range(r)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(start):
    stack = [start]
    visit[start[0]][start[1]] = True
    o, v = 0, 0
    now = backyard[start[0]][start[1]]
    if now == 'o':
        o += 1
    elif now == 'v':
        v += 1

    while stack:
        x, y = stack.pop()
        visit[x][y] = True

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0 <= nx < r and 0 <= ny < c):
                continue
            now = backyard[nx][ny]
            if not visit[nx][ny] and now != '#':
                visit[nx][ny] = True
                stack.append((nx, ny))
                if now == 'o':
                    o += 1
                elif now == 'v':
                    v += 1
    return o, v


n_o, n_v = 0, 0
for i in range(r):
    for j in range(c):
        if not visit[i][j] and backyard[i][j] != '#':
            tmp_o, tmp_v = dfs((i, j))
            if tmp_o > tmp_v:
                n_o += tmp_o
            else:
                n_v += tmp_v

print("{} {}".format(n_o, n_v))
