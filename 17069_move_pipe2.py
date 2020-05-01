"""
17069 파이프 옮기기

파이프를 옮길 수 있는 방법을 모두 구하여라.

알고리즘: DFS
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
house = [list(map(int, read().strip().split())) for _ in range(n)]
dxy = [(0, 1), (1, 1), (1, 0)]  # 우, 우하, 하


def dfs():
    cnt = 0
    stack = [(0, 1, 0, [(0, 1, 0)])]
    visit = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

    def check_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def check_horizontal(x, y, path):
        nx, ny = x, y + 1  # 가로
        if check_range(nx, ny):
            if house[nx][ny] == 0 and visit[nx][ny][0] != 1:
                visit[nx][ny][0] = 1
                return [(nx, ny, 0, path + [(nx, ny, 0)])]
        return []

    def check_vertical(x, y, path):
        nx, ny = x + 1, y
        if check_range(nx, ny):
            if house[nx][ny] == 0 and visit[nx][ny][1] != 1:
                visit[nx][ny][1] = 1
                return [(nx, ny, 1, path + [(nx, ny, 1)])]
        return []

    def check_diagonal(x, y, path):
        nx, ny = x + 1, y + 1
        if check_range(nx, ny):
            if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0 and visit[nx][ny][2] != 1:
                visit[nx][ny][2] = 1
                return [(nx, ny, 2, path + [(nx, ny, 2)])]
        return []

    while stack:
        rx, ry, d, path = stack.pop()
        if (rx, ry) == (n-1, n-1) or visit[rx][ry][d] == 2:
            for rx, ry, d in path:
                visit[rx][ry][d] = 2
            cnt += 1
            continue

        # direction 0: 가로
        # direction 1: 세로
        # direction 2: 대각선
        if d == 0:
            # horizontal
            stack.extend(check_horizontal(rx, ry, path))
            stack.extend(check_diagonal(rx, ry, path))
        elif d == 1:
            # vertical
            stack.extend(check_vertical(rx, ry, path))
            stack.extend(check_diagonal(rx, ry, path))
        else:
            # diagonal
            stack.extend(check_horizontal(rx, ry, path))
            stack.extend(check_vertical(rx, ry, path))
            stack.extend(check_diagonal(rx, ry, path))

    return cnt


print(dfs())
