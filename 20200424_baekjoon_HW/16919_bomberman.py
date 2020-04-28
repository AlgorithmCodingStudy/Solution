"""
16919 봄버맨 2

1. 봄버맨이 일부 칸에 폭탄설치
2. 1초 쉬고
3. 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
4. 1초가 지난 후 3초전에 설치된 폭탄 모두 폭발

알고리즘: 시뮬레이션


"""

import sys
read = sys.stdin.readline

r, c, n = map(int, read().split())
time = [[-1]*c for _ in range(r)]
state = []
for x in range(r):
    state.append(list(read().strip()))
    for y in range(c):
        if state[x][y] == 'O':
            time[x][y] = 2


def put_bomb():
    for i in range(r):
        for j in range(c):
            if time[i][j] == -1:
                time[i][j] = 3
                state[i][j] = 'O'


def bomb():
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    remove = set()
    for i in range(r):
        for j in range(c):
            if time[i][j] == 0:
                remove.add((i, j))
                for dx, dy in dxy:
                    nx, ny = i+dx, j+dy
                    if not (0 <= nx < r and 0 <= ny < c):
                        continue
                    remove.add((nx, ny))

    for i, j in remove:
        time[i][j] = -1
        state[i][j] = '.'


def nxt_time():
    for i in range(r):
        for j in range(c):
            if time[i][j] != -1:
                time[i][j] -= 1


for t in range(1, n):
    nxt_time()
    if t % 2:
        put_bomb()
    else:
        bomb()

for line in state:
    print("".join(line))
