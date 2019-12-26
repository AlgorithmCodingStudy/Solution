#-*- coding:utf-8 -*-

"""
7576 토마토

익은 토마토 주변 상하좌우의 익지 않은 토마토는 하루있으면 다 익는다.
며칠 지나면 모두 익는지 최소 일수를 구하라.

1은 익은 토마토
0은 익지 않은 토마토
-1은 토마토가 들어있지 않은 칸

모두 익을 최소 날짜 출력
모든 토마토가 익은 상태로 시작하면 0을 출력
모두 익을 수 없는 상황이면 -1

알고리즘: BFS

1. 익은 토마토의 위치와 개수, 빈공간 개수를 전부 찾는다.
2. 익은 토마토는 visit으로 처리하고 다음 익게될 예정인 토마토를 queue에 넣는다.
3. BFS를 시작한다.
4. visit 처리된 토마토가 전체공간 - 빈공간 개수가 되면 bfs를 끝낸다.

시간초과가 계속 뜨기때문에 정답코드와 하나씩 비교하며 바꿔가며 문제점을 파악해본다.

1. day를 queue에 계속 저장하지 않고 기존 box에 day를 저장하기 - 실패
2. 익지 않은 토마토 개수 세어 놓고 점점 줄여나가기 - 실패
3. queue 대신 deque 사용 - 성공...

python의 collections가 high performance container datatypes라고 설명하고 있는 만큼 빠르게 구현되었나보다.
앞으로는 collections를 사용하자.
"""
from collections import deque
import sys
read = sys.stdin.readline

m, n = map(int, read().strip().split())
box = []
start = []
empty = 0
yet = 0
for i in range(n):
    box.append(list(map(int, read().strip().split())))
    for j in range(m):
        if box[i][j] == 1:
            start.append((i, j))
        elif box[i][j] == -1:
            empty += 1
        else:
            yet += 1

n_tomato = m*n - empty

if not yet:
    print(0)
    sys.exit(0)
elif (len(start) + empty) == m*n:
    print(0)
    sys.exit(0)


def bfs():
    global yet
    day = 0
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    for node in start:
        q.append(node)

    while q:
        x, y = q.popleft()
        if yet == 0:
            print(day-1)
            sys.exit(0)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx, ny))
                    yet -= 1
                    day = max(box[nx][ny], day)

    print(-1)
    sys.exit(0)


bfs()
