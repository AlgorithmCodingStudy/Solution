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
from copy import deepcopy
import sys
read = sys.stdin.readline

n = int(read().strip())
blocks = [list(map(int, read().strip().split())) for _ in range(n)]


def nxt_blocks(now_blocks, depth):
    def gravity(line):
        line_divide = [[]]
        for v in line:
            if v == 0: continue
            else:
                if not line_divide[0]:
                    line_divide[0].append(v)
                elif v == line_divide[-1][0]:
                    line_divide[-1].append(v)
                else:
                    line_divide.append([v])

        result = []
        for line in line_divide:
            add = [sum(line[:2])] * (len(line) // 2)
            result.extend(add)
            if len(line) % 2 == 1:
                result.append(line[-1])

        result = result + [0]*(n-len(result))
        return result

    def up():
        for j in range(n):
            now = []
            for i in range(n):
                now.append(now_blocks[i][j])
            now = gravity(now)
            for i in range(n):
                nxt[i][j] = now[i]

    def down():
        for j in range(n):
            now = []
            for i in range(n):
                now.append(now_blocks[i][j])
            now = list(reversed(gravity(list(reversed(now)))))
            for i in range(n):
                nxt[i][j] = now[i]

    def left():
        for i in range(n):
            nxt[i] = gravity(now_blocks[i])

    def right():
        for i in range(n):
            nxt[i] = list(reversed(gravity(list(reversed(now_blocks[i])))))

    if depth == 5:
        value = list(map(max, now_blocks))
        value = max(value)

        global max_value
        max_value = max(value, max_value)
        return

    for fn in [up, down, left, right][:1]:
        nxt = [[0]*n for _ in range(n)]
        fn()
        nxt_blocks(nxt, depth+1)

max_value = 0
nxt_blocks(blocks, 0)
print(max_value)
