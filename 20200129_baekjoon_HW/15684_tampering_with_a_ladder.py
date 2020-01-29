"""
15684 사다리 조작

i번 세로선의 결과가 i가 나오도록 놓여져 있는 사다리에 추가해야하는 가로선 개수의 최솟값을 출력해야한다.
세로선 개수 N
가로선 개수 M
가로선을 놓을 수 있는 위치의 개수 H

알고리즘: 브루트 포스, BFS

1. 사다리 그리기
2. 테스트
3. 선그리기 반복 최대 3번
    1. 선그리기
    2. 테스트
        1. 선그리기
        2. 테스트
            1. 선그리기
            2. 테스트

(NxH)^3 = 300^3 = 270000
"""
from collections import deque
from copy import deepcopy
import sys
read = sys.stdin.readline

n, m, h = map(int, read().strip().split())
ladder = [[0]*n for _ in range(h)]
line = []
for _ in range(m):
    a, b = map(int, read().strip().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = -1


def check_ladder(_ladder):
    for j in range(n):
        now_j = j
        for i in range(h):
            if _ladder[i][now_j] == 0:
                continue
            elif _ladder[i][now_j] == 1:
                now_j += 1
            else:
                now_j -= 1
        if now_j != j:
            return False
    return True


def check_empty():
    empty_ = []
    for i in range(h):
        for j in range(n-1):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                empty_.append((i, j))
    return empty_


empty = check_empty()


def add_ladder():
    def add_nxt(now_depth, _ladder, _empty):
        for i, j in _empty:
            nxt_ladder = deepcopy(_ladder)
            nxt_empty = deepcopy(_empty)
            nxt_ladder[i][j], nxt_ladder[i][j+1] = 1, -1
            nxt_empty.remove((i, j))
            q.append((now_depth, nxt_ladder, nxt_empty))

    q = deque()
    add_nxt(1, ladder, empty)

    while q:
        depth, now_ladder, now_empty = q.popleft()
        if check_ladder(now_ladder):
            print(depth)
            sys.exit(0)
        else:
            if depth == 3:
                continue
            add_nxt(depth+1, now_ladder, now_empty)

    print(-1)


if check_ladder(ladder):
    print(0)
    sys.exit(0)

add_ladder()
