"""
13460 구슬 탈출2

red와 blue 구슬이 있는데 보드를 4 방향으로 기울여 구슬을 이동시킬 수 있다.
blue 구슬보다 red 구슬을 먼저 빼내려고 한다.
최소 횟수를 출력
동시에 빠지면 실패
기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을때 즉 사방이 막힌 곳?
10번이하로 빠지지 않으면 -1 출력

알고리즘: BFS

1. 3차원 BFS, 가로 세로 들어온 4방향
    1. start로 4방향 추가
    2. visit에 추가
        q의 길이만큼
        1. blue를 먼저 굴리면서 0에 빠지지 않는지 확인
        2. red를 굴리면서 0에 빠지지 않는지 확인
"""
from collections import deque
import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
board = []
for i in range(n):
    board.append(list(read().strip()))
    for j in range(m):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'O':
            hole = (i, j)

check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    def move(_x, _y, _dx, _dy):
        _c = 0
        while board[_x+_dx][_y+_dy] != '#' and board[_x][_y] != 'O':
            _x += _dx
            _y += _dy
            _c += 1
        return _x, _y, _c

    q = deque()
    q.append((blue, red, 0))
    check[blue[0]][blue[1]][red[0]][red[1]] = True

    while q:
        (bx, by), (rx, ry), d = q.popleft()
        if d >= 10:
            break
        for dx, dy in dxy:
            nrx, nry, nrc = move(rx, ry, dx, dy)
            nbx, nby, nbc = move(bx, by, dx, dy)
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(d+1)
                return
            if (nrx, nry) == (nbx, nby):
                if nrc > nbc:
                    nrx, nry = nrx-dx, nry-dy
                else:
                    nbx, nby = nbx-dx, nby-dy
            if not check[nbx][nby][nrx][nry]:
                check[nbx][nby][nrx][nry] = True
                q.append(((nbx, nby), (nrx, nry), d+1))
    print(-1)


bfs()
