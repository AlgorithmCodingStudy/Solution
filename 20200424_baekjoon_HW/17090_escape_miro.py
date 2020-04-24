"""
17090 미로 탈출하기

U (-1, 0)
R (0, 1)
D (1, 0)
L (0, -1)

칸에 적힌대로 움직이면 미로 경계 밖으로 나가는 칸의 개수를 구하라.

알고리즘: DFS, DP

(0, 0)부터 (n, m)까지 모두 검토한다.
상하좌우로 그 칸을 방문할 수 있으므로 3차원 visit 배열을 만들자.
visit에서 저장할 상태
    0: no visit
    1: visit
    2: escape available

즉, DFS로 경로를 모두 가져가다가 탈출하면 지나온 모든 경로는 2: escape available로 바꿔준다.
그냥 지나치는 곳은 1: visit으로 바꿔준다.
"""

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
miro = [list(read().strip()) for _ in range(n)]
visit = [[[0]*4 for _ in range(m)] for _ in range(n)]
direction = ['U', 'R', 'D', 'L']
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_miro(sx, sy):
    def check_range(x_, y_):
        return 0 <= x_ < n and 0 <= y_ < m

    def get_direction(x_, y_):
        return direction.index(miro[x_][y_])

    d = get_direction(sx, sy)
    path = [(sx, sy, d)]
    x, y = sx, sy
    visit[x][y][d] = 1
    while True:
        dx, dy = dxy[d]
        nx, ny = x+dx, y+dy
        if not check_range(nx, ny):
            for x, y, d in path:
                visit[x][y][d] = 2
            return True
        else:
            nd = get_direction(nx, ny)
            if visit[nx][ny][nd] == 0:
                visit[nx][ny][nd] = 1
                path.append((nx, ny, nd))
                x, y, d = nx, ny, nd
            elif visit[nx][ny][nd] == 1:
                return False
            else:
                for x, y, d in path:
                    visit[x][y][d] = 2
                return True


result = 0
for i in range(n):
    for j in range(m):
        k = direction.index(miro[i][j])
        if visit[i][j][k] == 0:
            result += check_miro(i, j)
        elif visit[i][j][k] == 2:
            result += 1
print(result)
