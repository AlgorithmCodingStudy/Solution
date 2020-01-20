"""
11559 Puyo Puyo

같은 색깔이 4개면 터진다.
터지고 나서 중력에 의해 아래로 내려가고 터질 게 또 있으면 연속으로 터진다.
1번의 상황에서 동시에 두 색깔이 터지더라도 1연쇄로 본다.

몇번 연쇄가 일어나는지 출력하라.

알고리즘: DFS or BFS

1. 기본적으로 끝날때까지 반복이 일어난다.
    1. 현재 상태에서 같은 색깔이 4개이상인 곳이 있는지 확인한다. (DFS)
    2. 4개 이상인 곳은 .으로 모두 바꾼다.
    3. 세로로 한줄씩 체크하며 . 다음으로 색깔이 나온다면 밑으로 당긴다.
    4. 연쇄 += 1

2. 연쇄를 출력
"""

import sys
read = sys.stdin.readline

stage = [list(read().strip()) for _ in range(12)]
stage = list(map(list, map(reversed, zip(*stage))))
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs_all():
    def dfs(start, clear):
        visit = {start: True}
        stack = [start]
        color = stage[start[0]][start[1]]
        if clear:
            stage[start[0]][start[1]] = '.'

        while stack:
            x, y = stack.pop()

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not(0 <= nx < 6 and 0 <= ny < 12):
                    continue
                if (nx, ny) not in visit and stage[nx][ny] == color:
                    stack.append((nx, ny))
                    visit[(nx, ny)] = True
                    if clear:
                        stage[nx][ny] = '.'

        return len(visit)

    flag = False
    global_visit = {}
    for i in range(6):
        for j in range(12):
            if stage[i][j] != '.' and (i, j) not in global_visit:
                cnt = dfs((i, j), False)
                if cnt >= 4:
                    dfs((i, j), True)
                    flag = True
            global_visit[(i, j)] = True

    return flag


def gravity():
    for line in stage:
        idx = 0
        for j in range(12):
            if line[idx] == '.':
                line.pop(idx)
            else:
                idx += 1

    for i in range(6):
        stage[i] += ['.']*(12-len(stage[i]))


chain = 0
nxt = True
while dfs_all():
    gravity()
    chain += 1

print(chain)
