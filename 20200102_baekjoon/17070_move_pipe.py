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
    stack = [((0, 0), (0, 1))]
    visit = {}

    def check_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def check_horizontal(x, y):
        nx, ny = x, y + 1  # 가로
        if check_range(nx, ny) and ((x, y), (nx, ny)) not in visit:
            if house[nx][ny] == 0:
                return (x, y), (nx, ny)  # 가로 추가

    def check_vertical(x, y):
        nx, ny = x + 1, y
        if check_range(nx, ny) and ((x, y), (nx, ny)) not in visit:
            if house[nx][ny] == 0:
                return (x, y), (nx, ny)  # 세로 추가

    def check_diagonal(x, y):
        diagonal = True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if check_range(nx, ny):
                if house[nx][ny] == 1:
                    diagonal = False
        if check_range(x + 1, y + 1):
            if diagonal and ((x, y), (x + 1, y + 1)) not in visit:
                return (x, y), (x + 1, y + 1)  # 대각선 추가

    def nxt_value(state):
        nxt_list = []
        # state 0: 가로
        # state 1: 세로
        # state 2: 대각선
        if state == 0:
            nxt_list.append(check_horizontal(*right))
            nxt_list.append(check_diagonal(*right))

        elif state == 1:
            nxt_list.append(check_vertical(*right))
            nxt_list.append(check_diagonal(*right))

        else:
            nxt_list.append(check_horizontal(*right))
            nxt_list.append(check_vertical(*right))
            nxt_list.append(check_diagonal(*right))

        for nxt in nxt_list:
            if not nxt:
                nxt_list.remove(None)
        if nxt_list:
            stack.extend(nxt_list)
        else:
            visit[(left, right)] = True

    while stack:
        tmp = stack.pop()
        if tmp == None: continue
        else: left, right = tmp
        if right == (n-1, n-1):
            cnt += 1

        if right[0] - left[0] == 1:
            if right[1] - left[1] == 1:
                # 대각선
                nxt_value(2)
            else:
                # 세로
                nxt_value(1)
        else:
            if right[1] - left[1] == 1:
                # 로
                nxt_value(0)

    return cnt


print(dfs())
