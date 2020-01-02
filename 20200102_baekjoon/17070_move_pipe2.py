#-*- coding:utf-8 -*-

"""
17070 파이프 옮기기

파이프를 (1, 1)에서 부터 (n, n)까지 옮길건데 방법이 3가지
가로일 때는 옆이랑 대각선으로 두가지
세로일 때는 아래랑 대각선으로 두가지
대각선일때는 옆이랑 아래랑 대각선으로 세가지

처음은 (1, 1), (1, 2)고 (n, n)으로 갈 수 있는 방법이 몇가지인지 구하자.
한쪽 끝이 (n, n)이면 종료
경우가 없으면 0 출력

알고리즘: DFS or BFS

1. DFS로 해보자.
"""

import sys
read = sys.stdin.readline

n = int(read().strip())
house = [list(map(int, read().strip().split())) for _ in range(n)]
dxy = [(0, 1), (1, 1), (1, 0)]  # 우, 우하, 하


def dfs():
    cnt = 0
    stack = [((0, 1), 0)]

    def check_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def check_horizontal(x, y):
        nx, ny = x, y + 1  # 가로
        if check_range(nx, ny):
            if house[nx][ny] == 0:
                return [((nx, ny), 0)]  # 가로 추가
        return []

    def check_vertical(x, y):
        nx, ny = x + 1, y
        if check_range(nx, ny):
            if house[nx][ny] == 0:
                return [((nx, ny), 1)]  # 세로 추가
        return []

    def check_diagonal(x, y):
        nx, ny = x + 1, y + 1
        if check_range(nx, ny):
            if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0:
                return [((nx, ny), 2)]  # 대각선 추가
        return []

    while stack:
        right, direction = stack.pop()
        if right == (n-1, n-1):
            cnt += 1

        # direction 0: 가로
        # direction 1: 세로
        # direction 2: 대각선
        if direction == 0:
            stack.extend(check_horizontal(*right))
            stack.extend(check_diagonal(*right))

        elif direction == 1:
            stack.extend(check_vertical(*right))
            stack.extend(check_diagonal(*right))

        else:
            stack.extend(check_horizontal(*right))
            stack.extend(check_vertical(*right))
            stack.extend(check_diagonal(*right))

    return cnt


print(dfs())
