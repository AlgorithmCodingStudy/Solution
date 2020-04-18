"""
14503 로봇 청소기

로봇 청소기가 청소하는 칸의 수를 구하라.

1. 현위치 청소
2. 왼쪽에 청소하지 않았으면 회전하고 한칸 전진
3. 네 방향 모두 청소되었거나 벽인 경우 한칸 후
4. 후진하려는데 뒤가 벽이면 끝

알고리즘: 시뮬레이션

0 북 1 동 2 남 3 서
3    0   1    2
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
r, c, d = map(int, read().split())
area = [list(map(int, read().split())) for _ in range(n)]
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0
while True:
    area[r][c] = 2
    for turn in range(4):
        left = d-1 if d > 0 else 3
        nr, nc = r+dxy[left][0], c+dxy[left][1]
        if not (0 <= nr < n and 0 <= nc < m) or area[nr][nc] == 1 or area[nr][nc] == 2:
            d = left
            non = True
            continue
        elif area[nr][nc] == 0:
            d = left
            r, c = nr, nc
            non = False
            break

    if non:
        r, c = r-dxy[d][0], c-dxy[d][1]
        if area[r][c] == 1:
            break

for i in range(n):
    for j in range(m):
        if area[i][j] == 2:
            result += 1

print(result)
