"""
12100 2048 (easy)

2048 게임을 하는데 상하좌우로 5번 움직여서 만들 수 있는 가장 큰 블록 값을 구하라.

알고리즘: 시뮬레이션, DFS

1. 상하좌우로 움직이는 함수 구현
2. 재귀함수 호출
    1. depth가 5면
        1. 최대 비교
    2. 방향에 따른 처리
    3. 상하좌우로 네번 재귀함수 호출
3. 출력
"""
from itertools import chain

import sys
read = sys.stdin.readline

n = int(read().strip())
blocks = [list(map(int, read().strip().split())) for _ in range(n)]


def move_blocks(now_blocks, depth, direction):
    # 위 아래 경우에는 transpose
    if direction == 0 or direction == 1:
        now_blocks = list(map(list, zip(*now_blocks)))

    nxt_blocks = []
    for line in now_blocks:
        non_zero = [i for i in line if i]

        # 왼쪽으로 move
        if direction == 0 or direction == 3:
            for i in range(1, len(non_zero)):
                if non_zero[i-1] == non_zero[i]:
                    non_zero[i-1] += non_zero[i]
                    non_zero[i] = 0

            non_zero = [i for i in non_zero if i]
            non_zero = non_zero + [0]*(n-len(non_zero))

        else:
            for i in range(len(non_zero)-1, 0, -1):
                if non_zero[i-1] == non_zero[i]:
                    non_zero[i] += non_zero[i-1]
                    non_zero[i-1] = 0

            non_zero = [i for i in non_zero if i]
            non_zero = [0] * (n - len(non_zero)) + non_zero

        nxt_blocks.append(non_zero)

    if direction == 0 or direction == 1:
        nxt_blocks = list(map(list, zip(*nxt_blocks)))

    if depth == 5:
        global max_value
        max_value = max(max_value, max(list(chain(*nxt_blocks))))
        return

    move_blocks(nxt_blocks, depth+1, 0)
    move_blocks(nxt_blocks, depth+1, 1)
    move_blocks(nxt_blocks, depth+1, 2)
    move_blocks(nxt_blocks, depth+1, 3)


max_value = 0
for i in range(4):
    move_blocks(blocks, 1, i)
print(max_value)
