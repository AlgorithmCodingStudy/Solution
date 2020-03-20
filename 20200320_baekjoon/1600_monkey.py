"""
1600 말이 되고픈 원숭이

원숭이가 이동하는데 체스말처럼 이동할 수 있고 상하좌우로 이동할 수 있다.
다만 말처럼 이동할 수 있는 횟수는 K로 제한되어 있다.
말처럼 이동할 때는 장애물을 넘어갈 수 있다.
0, 0에서  n, m까지 이동할 수 있는 최소 횟수는?
이동 할 수 없다면 -1을 출력

알고리즘: DFS

1. 최소 횟수는 말로 이동하는 횟수이므로 결국 모든 경우를 확인해야함.
2. queue에는 현재 위치와 현재 k를 저장
    visit 대신 check 배열을 만든다.
    check 배열에는 현재 말로 이동한 횟수를 저장한다.
    만약 가려고 하는 곳의 값이 k보다 크다면 이동
3. 현재 k가 k라면 상하좌우만 이동
4. k보다 작으면 말처럼 이동도 포함
"""
from collections import deque
import sys
read = sys.stdin.readline

k = int(read())
w, h = map(int, read().split())
area = [list(map(int, read().split())) for _ in range(h)]
check = [[[-1]*(k+1) for _ in range(w)] for _ in range(h)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dxy_h = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def bfs():
    def check_range(_x, _y):
        return 0 <= _x < h and 0 <= _y < w

    q = deque([(0, 0, 0)])
    check[0][0][0] = 0
    cnt = 0

    while q:
        qsize = len(q)
        for _ in range(qsize):
            x, y, now_k = q.popleft()
            if (x, y) == (h-1, w-1):
                return cnt

            if now_k < k:
                for dx, dy in dxy_h:
                    nx, ny = x+dx, y+dy
                    if (not check_range(nx, ny)) or area[nx][ny] == 1:
                        continue
                    if check[nx][ny][now_k+1] == -1:
                        q.append((nx, ny, now_k+1))
                        check[nx][ny][now_k+1] = cnt
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if (not check_range(nx, ny)) or area[nx][ny] == 1:
                    continue
                if check[nx][ny][now_k] == -1:
                    q.append((nx, ny, now_k))
                    check[nx][ny][now_k] = cnt
        cnt += 1
    return -1

print(bfs())

# def dfs():
#     def check_range(_x, _y):
#         return 0 <= _x < h and 0 <= _y < w
#
#     q = [(0, 0, 0)]
#     check[0][0] = 0
#
#     while q:
#         x, y, now_k = q.pop()
#
#         if now_k < k:
#             for dx, dy in dxy_h:
#                 nx, ny = x+dx, y+dy
#                 if not check_range(nx, ny) or area[nx][ny] == 1:
#                     continue
#                 if now_k+1 < check[nx][ny]:
#                     q.append((nx, ny, now_k+1))
#                     check[nx][ny] = now_k+1
#         for dx, dy in dxy:
#             nx, ny = x+dx, y+dy
#             if not check_range(nx, ny) or area[nx][ny] == 1:
#                 continue
#             if now_k < check[nx][ny]:
#                 q.append((nx, ny, now_k))
#                 check[nx][ny] = now_k


