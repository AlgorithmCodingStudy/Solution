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

check_blue = [[[-1]*4 for _ in range(m)] for _ in range(n)]
check_red = [[[-1]*4 for _ in range(m)] for _ in range(n)]

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    def check_range(x_, y_):
        return 0 <= x_ < n and 0 <= y_ < m

    q = deque()
    for direction in range(4):
        q.append((blue, red, direction))

    for cnt in range(10):
        qsize = len(q)
        state = True
        for _ in range(qsize):
            (bx, by), (rx, ry), d = q.popleft()

            while True:
                bx, by = bx+dxy[d][0], by+dxy[d][1]
                if not check_range(bx, by): break
                check_blue[bx][by][d] = 1

                if board[bx][by] == 'O':
                    state = False
                    break
                elif board[bx][by] == '#':
                    break
            if not state:
                continue

            while True:
                rx, ry = rx+dxy[d][0], ry+dxy[d][1]
                if not check_range(rx, ry): break
                check_red[rx][ry][d] = 1
                if board[rx][ry] == 'O':
                    return cnt+1
                elif board[rx][ry] == '#':
                    break

            for d in range(4):
                q.append(((bx, by), (rx, ry), d))

    return -1


print(bfs())

